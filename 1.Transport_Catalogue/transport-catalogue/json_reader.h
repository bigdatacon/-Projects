#pragma once

#include <sstream>
#include <string>
#include <deque>
#include <iostream>
#include <vector>

#include "transport_catalogue.h"
#include "domain.h"
#include "json.h"
#include "geo.h"
#include "map_renderer.h"
#include "json_builder.h"
#include "transport_router.h"

inline json::Document LoadJSON(const std::string& s) {
	std::istringstream strm(s);
	return json::Load(strm);
}

inline std::string Print(const json::Node& node) {
	std::ostringstream out;
	Print(json::Document{ node }, out);
	return out.str();
}

namespace transport_catalogue {

	class InputReaderJson {
	public:
		explicit InputReaderJson(std::istream& is);

		void ReadInputJsonBaseRequest();
		void ReadInputJsonStatRequest();
		void ReadInputJsonRenderSettings();

		void ReadInputJsonRouteSettings();
		void ReadInputJsonSerializeSettings();


		void ReadInputJsonRequest();

		// Добавлено на 15 спринт 
		void ReadInputJsonRequestForFillBase();
		void ReadInputJsonRequestForReadBase();

		void UpdStop(TransportCatalogue& tc);

		void UpdBus(TransportCatalogue& tc);

		void UpdStopDist(TransportCatalogue& tc);

        void ManageOutputRequests(TransportCatalogue& tc, MapRenderer& mr, graph::ActivityProcessor& actprocess);
        void HandleBusRequest(const OutputRequest& request, const TransportCatalogue& tc, json::Array& queries);
        void HandleStopRequest(const OutputRequest& request, const TransportCatalogue& tc, json::Array& queries);
        void HandleMapRequest(const OutputRequest& request, const TransportCatalogue& tc, MapRenderer& mr, json::Array& queries);
        void HandleRouteRequest(const OutputRequest& request, const TransportCatalogue& tc, graph::ActivityProcessor& actprocess, json::Array& queries);
        RenderSettings GetRenderSettings();

		void UpdRouteSettings(TransportCatalogue& tc);
		// добавлено на 15 спринт
		void UpdSerializeSettings(TransportCatalogue& tc);

		std::string GetSerializeFilePath();


	private:
		std::istream& is_;

		std::deque<OutputRequest> out_req_;

		std::deque<domain::BusDescription> upd_req_bus_;
		std::deque<domain::Stop> upd_req_stop_;
		std::vector<domain::StopDistancesDescription> distances_;
        RenderSettings render_settings_;
		json::Document load_;
		domain::RouteSettings route_settings_;
		std::string serialize_file_path_;

	};

}



