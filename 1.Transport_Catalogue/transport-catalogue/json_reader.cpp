#include "transport_catalogue.h"
#include "json.h"
#include "geo.h"
#include "svg.h"
#include "json_reader.h"
#include "json_builder.h"

using namespace json;
using namespace std;
using namespace transport_catalogue::domain;
using namespace svg;

namespace transport_catalogue {

	svg::Color GetColor(const json::Node& el) {
		svg::Color color;

		if (el.IsString()) {
			color = el.AsString();
		}
		else {
			if (el.AsArray().size() == 3) {
				Rgb rgb;
				rgb.red_ = static_cast<uint8_t>(el.AsArray()[0].AsInt());
				rgb.green_ = static_cast<uint8_t>(el.AsArray()[1].AsInt());
				rgb.blue_ = static_cast<uint8_t>(el.AsArray()[2].AsInt());
				color = rgb;
			}
			else if (el.AsArray().size() == 4) {
				Rgba rgba;
				rgba.red_ = static_cast<uint8_t>(el.AsArray()[0].AsInt());
				rgba.green_ = static_cast<uint8_t>(el.AsArray()[1].AsInt());
				rgba.blue_ = static_cast<uint8_t>(el.AsArray()[2].AsInt());
				rgba.opacity_ = el.AsArray()[3].AsDouble();
				color = rgba;
			}
		}


		return color;

	}


	InputReaderJson::InputReaderJson(istream& is) : is_(is), load_(json::Load(is)) {

	}


	void InputReaderJson::ReadInputJsonBaseRequest() {
		const auto& json_array = ((load_.GetRoot()).AsDict()).at("base_requests"s);
		for (const auto& file : json_array.AsArray()) {
			const auto& json_obj = file.AsDict();
			if (json_obj.at("type"s) == "Stop"s) {
				Stop stopjson;
				stopjson.stop_name = json_obj.at("name").AsString();
				stopjson.coordinates.lat = json_obj.at("latitude").AsDouble();
				stopjson.coordinates.lng = json_obj.at("longitude").AsDouble();

				StopDistancesDescription input_stop_dist;
				input_stop_dist.stop_name = json_obj.at("name").AsString();
				auto heighbors = json_obj.at("road_distances");

				for (auto el : heighbors.AsDict()) {
					input_stop_dist.distances.push_back(make_pair(el.first, el.second.AsInt()));

				}
				upd_req_stop_.push_back(stopjson);
				distances_.push_back(input_stop_dist);
			}
			else if (json_obj.at("type"s) == "Bus"s) {
				BusDescription bs;
				auto stop_list = json_obj.at("stops").AsArray();
				for (auto el : stop_list) {

					bs.stops.push_back(el.AsString());

				}
				bs.bus_name = json_obj.at("name").AsString();

				auto trip = json_obj.at("is_roundtrip").AsBool();
				if (trip) {
					bs.type = "true"s;
				}
				else { bs.type = "false"s; }

				upd_req_bus_.push_back(bs);

			}
		}

	}

	void InputReaderJson::ReadInputJsonStatRequest() {
		const auto& json_array_out = ((load_.GetRoot()).AsDict()).at("stat_requests"s);
		if (!json_array_out.IsNull()) {
			for (const auto& file : json_array_out.AsArray()) {
				const auto& json_obj = file.AsDict();
				OutputRequest outputstopjson;
				if (json_obj.at("type").AsString() == "Map"s) {
					outputstopjson.id = json_obj.at("id").AsInt();
					outputstopjson.type = json_obj.at("type").AsString();
					out_req_.push_back(outputstopjson);
				}
				else if (json_obj.at("type").AsString() == "Route"s) {
					outputstopjson.id = json_obj.at("id").AsInt();
					outputstopjson.type = json_obj.at("type").AsString();
					outputstopjson.from = json_obj.at("from").AsString();
					outputstopjson.to = json_obj.at("to").AsString();
					out_req_.push_back(outputstopjson);
				}
				else {
					outputstopjson.name = json_obj.at("name").AsString();
					outputstopjson.id = json_obj.at("id").AsInt();
					outputstopjson.type = json_obj.at("type").AsString();
					out_req_.push_back(outputstopjson);
				}
			}
		}
	}

	void InputReaderJson::ReadInputJsonRenderSettings() {

		const auto& json_array_render = ((load_.GetRoot()).AsDict()).at("render_settings"s).AsDict();
		if (json_array_render.find("width") != json_array_render.end()) {
            render_settings_.width_ = json_array_render.find("width")->second.AsDouble();
		}

		if (json_array_render.find("height") != json_array_render.end()) {
            render_settings_.height_ = json_array_render.find("height")->second.AsDouble();
		}

		if (json_array_render.find("padding") != json_array_render.end()) {
            render_settings_.padding_ = json_array_render.find("padding")->second.AsDouble();
		}

		if (json_array_render.find("line_width") != json_array_render.end()) {
            render_settings_.line_width_ = json_array_render.find("line_width")->second.AsDouble();
		}

		if (json_array_render.find("stop_radius") != json_array_render.end()) {
            render_settings_.stop_radius_ = json_array_render.find("stop_radius")->second.AsDouble();
		}

		if (json_array_render.find("bus_label_font_size") != json_array_render.end()) {
            render_settings_.bus_label_font_size_ = json_array_render.find("bus_label_font_size")->second.AsDouble();
		}

        if (json_array_render.find("bus_label_offset") != json_array_render.end()) {

            auto el = json_array_render.find("bus_label_offset")->second.AsArray();
            render_settings_.bus_label_offset_ = std::make_pair(el[0].AsDouble(), el[1].AsDouble() );
        }

        if (json_array_render.find("stop_label_offset") != json_array_render.end()) {
            auto el = json_array_render.find("stop_label_offset")->second.AsArray();
            render_settings_.stop_label_offset_ = std::make_pair(el[0].AsDouble(), el[1].AsDouble() );

        }

        /*
		if (json_array_render.find("bus_label_offset") != json_array_render.end()) {

			for (auto el : json_array_render.find("bus_label_offset")->second.AsArray()) { render_data_.bus_label_offset.push_back(el.AsDouble()); }
		}

		if (json_array_render.find("stop_label_offset") != json_array_render.end()) {

			for (auto el : json_array_render.find("stop_label_offset")->second.AsArray()) { render_data_.stop_label_offset.push_back(el.AsDouble()); }
		}
        */

		if (json_array_render.find("stop_label_font_size") != json_array_render.end()) {
            render_settings_.stop_label_font_size_ = json_array_render.find("stop_label_font_size")->second.AsDouble();
		}

        if (json_array_render.find("underlayer_color") != json_array_render.end()) {
            render_settings_.underlayer_color_ = GetColor(json_array_render.find("underlayer_color")->second);

        }

		if (json_array_render.find("underlayer_width") != json_array_render.end()) {
            render_settings_.underlayer_width_ = json_array_render.find("underlayer_width")->second.AsDouble();
		}

		if (json_array_render.find("color_palette") != json_array_render.end()) {
			for (auto el : json_array_render.find("color_palette")->second.AsArray()) {

                render_settings_.color_palette_.push_back(GetColor(el));

			}

		}

	}

	void InputReaderJson::ReadInputJsonRouteSettings() {
		const auto& json_array_out = ((load_.GetRoot()).AsDict()).at("routing_settings"s);
		const auto& json_obj = json_array_out.AsDict();
		route_settings_.bus_velocity = json_obj.at("bus_velocity").AsDouble();
		route_settings_.bus_wait_time = json_obj.at("bus_wait_time").AsDouble();

	}

	void InputReaderJson::ReadInputJsonSerializeSettings() {
		const auto& json_array_out = ((load_.GetRoot()).AsDict()).at("serialization_settings"s);
		const auto& json_obj = json_array_out.AsDict();
		serialize_file_path_ = json_obj.at("file").AsString();
	}

	void InputReaderJson::ReadInputJsonRequest() {
		ReadInputJsonBaseRequest();
		//ReadInputJsonStatRequest();
		ReadInputJsonRenderSettings();
		ReadInputJsonRouteSettings();
		ReadInputJsonSerializeSettings();
	}


	void InputReaderJson::ReadInputJsonRequestForFillBase() {
		ReadInputJsonBaseRequest();
		ReadInputJsonRenderSettings();
		ReadInputJsonRouteSettings();
		ReadInputJsonSerializeSettings();
	}

	void InputReaderJson::ReadInputJsonRequestForReadBase() {
		ReadInputJsonSerializeSettings();
		ReadInputJsonStatRequest();
	}



	void InputReaderJson::UpdStop(TransportCatalogue& tc) {
		for (int i = 0; i < static_cast<int>(upd_req_stop_.size()); ++i) {
			tc.AddStop(upd_req_stop_[i]);
		}
	}

	void InputReaderJson::UpdStopDist(TransportCatalogue& tc) {
		for (int i = 0; i < static_cast<int>(distances_.size()); ++i) {
			tc.AddStopDistance(distances_[i]);
		}
	}

	void InputReaderJson::UpdBus(TransportCatalogue& tc) {
		for (int i = 0; i < static_cast<int>(upd_req_bus_.size()); ++i) {
			tc.AddBus(upd_req_bus_[i]);
		}
	}

	/*graph::ActivityProcessor<Weight>& actprocess )*/



    RenderSettings InputReaderJson::GetRenderSettings() {
		return render_settings_;
	}


	void InputReaderJson::UpdRouteSettings(TransportCatalogue& tc) {

		tc.AddRouteSettings(route_settings_);

	}

	void InputReaderJson::UpdSerializeSettings(TransportCatalogue& tc) {

		tc.AddSerializePathToFile(serialize_file_path_);

	}

	std::string InputReaderJson::GetSerializeFilePath() {
		return serialize_file_path_;
	}

    void InputReaderJson::ManageOutputRequests(TransportCatalogue& tc, MapRenderer& mr, graph::ActivityProcessor& actprocess) {
        std::ostream& out = std::cout;
        json::Array queries;

        for (const auto& el : out_req_) {
            if (el.type == "Bus"s) {
                HandleBusRequest(el, tc, queries);
            } else if (el.type == "Stop"s) {
                HandleStopRequest(el, tc, queries);
            } else if (el.type == "Map"s) {
                HandleMapRequest(el, tc, mr, queries);
            } else if (el.type == "Route"s) {
                HandleRouteRequest(el, tc, actprocess, queries);
            }
        }

        json::Print(json::Document{ queries }, out);
    }

    void InputReaderJson::HandleBusRequest(const OutputRequest& request, const TransportCatalogue& tc, json::Array& queries) {
        const Bus* bus_resp = tc.FindBus(request.name);
        if (bus_resp == nullptr) {
            json::Node answer_empty_bus = json::Builder{}
                    .StartDict()
                    .Key("error_message").Value("not found"s)
                    .Key("request_id").Value(request.id)
                    .EndDict().Build();

            queries.emplace_back(answer_empty_bus);
        } else {
            AllBusInfoBusResponse r = tc.GetAllBusInfo(request.name);

            json::Node non_empty_bus = json::Builder{}
                    .StartDict()
                    .Key("curvature").Value(r.route_curvature)
                    .Key("request_id").Value(request.id)
                    .Key("route_length").Value(r.route_length)
                    .Key("stop_count").Value(r.quant_stops)
                    .Key("unique_stop_count").Value(r.quant_uniq_stops)
                    .EndDict().Build();

            queries.emplace_back(non_empty_bus);
        }
    }

    void InputReaderJson::HandleStopRequest(const OutputRequest& request, const TransportCatalogue& tc, json::Array& queries) {
        const Stop* myStop = tc.FindStop(request.name);
        if (myStop == nullptr) {
            json::Node answer_empty_stop = json::Builder{}
                    .StartDict()
                    .Key("error_message").Value("not found"s)
                    .Key("request_id").Value(request.id)
                    .EndDict().Build();

            queries.emplace_back(answer_empty_stop);
        } else {
            std::set<std::string> r = tc.GetStopInfo(request.name);
            json::Array routes;
            std::copy(r.begin(), r.end(), std::back_inserter(routes));

            json::Node answer_stop = json::Builder{}
                    .StartDict()
                    .Key("buses").Value(routes)
                    .Key("request_id").Value(request.id)
                    .EndDict().Build();

            queries.emplace_back(answer_stop);
        }
    }

    void InputReaderJson::HandleMapRequest(const OutputRequest& request, const TransportCatalogue& tc, MapRenderer& mr, json::Array& queries) {
        std::string map_str = mr.DrawRouteGetDoc(tc);

        json::Node answer_empty_map = json::Builder{}
                .StartDict()
                .Key("map").Value(map_str)
                .Key("request_id").Value(request.id)
                .EndDict().Build();

        queries.emplace_back(answer_empty_map);
    }

    void InputReaderJson::HandleRouteRequest(const OutputRequest& request, const TransportCatalogue& tc, graph::ActivityProcessor& actprocess, json::Array& queries) {
        if (tc.FindStop(request.from) && tc.FindStop(request.to)) {
            std::optional<graph::DestinatioInfo> route = actprocess.GetRouteAndBuses(request.from, request.to);
            std::vector<json::Node> array;

            int request_id = request.id;
            double total_time = 0;
            std::string error_message = "not found"s;

            if (route.has_value()) {
                total_time = route.value().all_time;
                std::vector<std::variant<graph::BusActivity, graph::WaitingActivity>> final_route = route.value().route;

                for (const auto& el : final_route) {
                    if (std::holds_alternative<graph::BusActivity>(el)) {
                        graph::BusActivity act = std::get<graph::BusActivity>(el);

                        json::Node bus_route_description = json::Builder{}
                                .StartDict()
                                .Key("bus").Value(act.bus_name)
                                .Key("span_count").Value(act.span_count)
                                .Key("time").Value(act.time)
                                .Key("type").Value("Bus")
                                .EndDict().Build();

                        array.push_back(bus_route_description);
                    } else {
                        graph::WaitingActivity act = std::get<graph::WaitingActivity>(el);

                        json::Node bus_route_description = json::Builder{}
                                .StartDict()
                                .Key("stop_name").Value(act.stop_name_from)
                                .Key("time").Value(act.time)
                                .Key("type").Value("Wait")
                                .EndDict().Build();

                        array.push_back(bus_route_description);
                    }
                }

                json::Node final_route_description = json::Builder{}
                        .StartDict()
                        .Key("items").Value(array)
                        .Key("request_id").Value(request_id)
                        .Key("total_time").Value(total_time)
                        .EndDict().Build();

                queries.emplace_back(final_route_description);
            } else {
                json::Node final_route_description = json::Builder{}
                        .StartDict()
                        .Key("request_id").Value(request_id)
                        .Key("error_message").Value(error_message)
                        .EndDict().Build();

                queries.emplace_back(final_route_description);
            }
        } else {
            int request_id = request.id;
            std::string error_message = "not found"s;
            json::Node final_route_description = json::Builder{}
                    .StartDict()
                    .Key("request_id").Value(request_id)
                    .Key("error_message").Value(error_message)
                    .EndDict().Build();

            queries.emplace_back(final_route_description);
        }
    }


}