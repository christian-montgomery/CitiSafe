# CitiSafe – Real-Time Multimodal Urban Hazard Detection 🚨

CitiSafe is a real-time AI-powered system that analyzes live traffic cameras
and user-submitted images to detect urban hazards such as:

- Accidents
- Flooding
- Fires/Smoke
- Road obstructions
- Crowds

It uses HuggingFace vision models (Object Detection, Depth Estimation,
Captioning, Classification, VQA) to determine hazard severity and provide
safe routing across the city.

## Features
- Real-time object detection (crashes, debris)
- Flood depth measurement from a single image
- Fire/smoke probability classification
- Image captioning for automatic scene summaries
- Visual question answering ("Is this area safe?")
- Live Mapbox hazard map
- Safe route generation avoiding danger zones
- User photo uploads + camera feed ingestion

## Tech Stack
### Backend
- FastAPI (Python)
- HuggingFace Transformers + Diffusers
- ONNX Runtime
- PostgreSQL + PostGIS
- Redis Streams
- Docker

### Frontend
- React + Vite
- Mapbox GL JS
- WebSockets

## Getting Started
- `docker-compose up` to start backend + DB
- `npm install && npm run dev` in frontend to launch UI
