# 🎡 Spin Platform

A probabilistic gaming system built using FastAPI and React.

## ⚙️ Current Status
- ✅ Backend setup complete
- ✅ Spin API working  
- ⏳ Frontend integration upcoming

## ▶️ Run Locally

### Backend
cd backend
venv\Scripts\activate
python -m uvicorn main:app --reload

## 🧱 Tech Stack
- FastAPI
- React
- PostgreSQL (planned)
- Redis (planned)

## 🚀 Planned Features
- Weighted probability engine
- RTP control
- Analytics dashboard
- Real-time updates

## 📅 Day 2 – Backend API Development

- Set up backend server using FastAPI  
- Implemented core API endpoints:
  - `/` → health check for API status  
  - `/spin` → returns a random spin result  
  - `/options` → fetch all available wheel options  
- Integrated random selection logic using Python (`random.choice`)  
- Structured API responses with success flag and message  
- Tested all endpoints using Swagger UI (`/docs`)  
- Improved API readability with proper routing and response format  

### ✅ Outcome
- Backend server is fully functional  
- APIs are testable and ready for frontend integration  
- Established foundation for dynamic and scalable spin logic  

## 📅 Day 3 – Dynamic Wheel & Weighted Logic

- Replaced static options with dynamic `wheel_data` structure  
- Implemented weighted probability system using `random.choices`  
- Created POST API:
  - `/set-options` → allows updating wheel options dynamically  
- Integrated request body handling using Pydantic models  
- Enabled dynamic backend behavior (no hardcoded values)  
- Verified probability behavior through repeated API testing  

### ✅ Outcome
- Backend now supports dynamic configuration  
- Spin results follow controlled probability distribution  
- Foundation ready for database integration and advanced logic  