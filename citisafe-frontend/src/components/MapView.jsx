import { useEffect, useRef } from "react";
import mapboxgl from "mapbox-gl";
import { fetchHazards } from "../api/hazards.js";

mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN;

export default function MapView() {
    const mapRef = useRef(null);
    const mapContainerRef = useRef(null);

    useEffect(() => {
        if (mapRef.current) return; // Initialize map only once

        mapRef.current = new mapboxgl.Map({
            container: mapContainerRef.current,
            style: "mapbox://styles/mapbox/dark-v11",
            center: [-83.0458, 42.3314], // Detroit default
            zoom: 12,
        });

        loadHazards();
    }, []);

    async function loadHazards() {
        const hazards = await fetchHazards();
        hazards.forEach(h => addHazardToMap(h));
    }

    function addHazardToMap(hazard) {
        new mapboxgl.Marker({ color: hazard.severity >= .7 ? 'red' : 'yellow'})
            .setLngLat([hazard.location.lon, hazard.location.lat])
            .setPopup(new mapboxgl.Popup().setText(`${hazard.type}: ${hazard.description}`))
            .addTo(mapRef.current);
    }

    return <div ref={mapContainerRef} style={{ width: "100%", height: "100vh" }} />;
}