#pragma once

#include "transport_catalogue.h"
#include "transport_catalogue.pb.h"

#include "svg.pb.h"

#include "map_renderer.h"
#include "map_renderer.pb.h"

#include "transport_router.h"
#include "transport_router.pb.h"

#include <iostream>
namespace transport_catalogue {
    namespace serialization {

        struct SerializationSettings {
            std::string file_name;
        };
        // Структура используется в 46 строке в возвращаемом аргументе
        struct Catalogue {
            transport_catalogue::TransportCatalogue transport_catalogue_;
            transport_catalogue::RenderSettings render_settings_;
            domain::RouteSettings routing_settings_;
        };


        template<typename It>
        uint32_t СalculateId(It start, It end, std::string_view name);

        transport_catalogue_protobuf::TransportCatalogue
        TransportCatalogueSerialize(const transport_catalogue::TransportCatalogue &transport_catalogue);

        transport_catalogue::TransportCatalogue TransportCatalogueDeserialize(
                const transport_catalogue_protobuf::TransportCatalogue &transport_catalogue_proto);

        transport_catalogue_protobuf::Color ColorSerialize(const svg::Color &tc_color);

        svg::Color ColorDeserialize(const transport_catalogue_protobuf::Color &color_proto);

        transport_catalogue_protobuf::RenderSettings
        RenderSettingsSerialize(const transport_catalogue::RenderSettings &render_settings);

        transport_catalogue::RenderSettings
        RenderSettingsDeserialize(const transport_catalogue_protobuf::RenderSettings &render_settings_proto);

        transport_catalogue_protobuf::RouteSettings
        RoutingSettingsSerialize(const domain::RouteSettings &routing_settings);

        domain::RouteSettings
        RoutingSettingsDeserialize(const transport_catalogue_protobuf::RouteSettings &routing_settings_proto);

        void CatalogueSerialize(const transport_catalogue::TransportCatalogue &transport_catalogue,
                                const transport_catalogue::RenderSettings &render_settings,
                                const domain::RouteSettings &routing_settings,
                                std::ostream &out);

        Catalogue CatalogueDeserialize(std::istream &in);

    }//end namespace serialization

}//end namespace transport_catalogue