# Voltora ⚡ — Electric Bike Rental, Buying & Selling Platform

> **"Power Your Next Ride ⚡"**  
> *Rent. Buy. Sell. Go electric.*

Voltora is a premier, full-stack electric mobility platform built for India, launching in Hyderabad. It empowers users to rent EV bikes by the hour/day/week/month, buy new or verified pre-owned EV two-wheelers, and list their own electric bikes with document verification and admin curation.

---

## 🏗️ Architecture & Monorepo Structure

```text
EV bike/
├── backend/                  # Python / Django REST Framework API
│   ├── manage.py
│   ├── voltora_backend/      # Core project configuration & settings
│   │   ├── __init__.py
│   │   ├── settings.py       # JWT, CORS, DRF-Spectacular, Database config
│   │   ├── urls.py           # Root API routing & Swagger docs
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── apps/                 # Modular Django apps
│   │   ├── users/            # Custom User model (customer/seller/admin), Auth, KYC
│   │   ├── bikes/            # Bike models, specifications, brands, gallery images
│   │   ├── rentals/          # Rental plans, bookings, availability checker, late fees
│   │   ├── marketplace/      # Sell listings, seller approval, inquiries, orders
│   │   ├── payments/         # Razorpay service layer, refunds, commissions, webhooks
│   │   ├── locations/        # Hyderabad pickup stations (Hitec City, Gachibowli, etc.)
│   │   ├── reviews/          # Verified bike & seller ratings/reviews
│   │   ├── notifications/    # In-app notifications & transactional alerts
│   │   ├── subscriptions/    # Commuter, student & gig worker monthly rental packs
│   │   ├── wishlist/         # Saved bikes & marketplace listings
│   │   └── support/          # Inquiries, contact tickets & help desk
│   ├── media/                # Local development uploads (KYC docs, bike photos)
│   ├── static/               # Django static assets
│   ├── requirements.txt      # Python dependencies
│   ├── .env.example          # Sample environment variables
│   └── .env                  # Backend secrets (gitignored)
│
├── frontend/                 # Next.js 14+ (App Router), TypeScript, Tailwind CSS
│   ├── public/               # Static assets & brand SVG logos
│   │   └── logo.svg          # Voltora electric lightning bolt emblem & wordmark
│   ├── src/
│   │   ├── app/              # Next.js App Router pages
│   │   │   ├── layout.tsx    # Root layout with fonts, Navbar, Footer & Providers
│   │   │   ├── page.tsx      # High-converting Homepage
│   │   │   ├── (auth)/
│   │   │   │   ├── login/    # Role-aware login with 1-click quick-demo credentials
│   │   │   │   └── register/ # Customer / Seller onboarding registration
│   │   │   ├── rent/         # Rent EV bikes catalog, date/hub filters, map preview
│   │   │   ├── buy/          # Buy new & certified used EVs with comparison tool
│   │   │   ├── sell/         # Multi-step sell listing submission & KYC
│   │   │   ├── bikes/[id]/   # High-detail bike view, specs, 360 gallery & booking
│   │   │   ├── bookings/     # Booking checkout, price calculator, Razorpay
│   │   │   ├── account/      # User profile, KYC verification & settings
│   │   │   ├── admin/        # Custom React Admin Management Portal
│   │   │   └── owner/        # Seller & Fleet Owner dashboard
│   │   ├── components/       # Reusable UI component library
│   │   │   ├── ui/           # Buttons, Inputs, Badges, Modals, Range sliders
│   │   │   ├── layout/       # Navbar, Footer, CitySelector, MobileDrawer
│   │   │   ├── home/         # Hero, ServiceCards, Stats, RangeEstimator, HowItWorks
│   │   │   └── bikes/        # BikeCard, FilterSidebar, SpecsGrid, ComparisonTable
│   │   ├── context/          # React Context (AuthContext, CityContext, Cart/Booking)
│   │   ├── services/         # Typed API clients consuming Django REST endpoints
│   │   └── types/            # TypeScript interfaces matching backend models
│   ├── tailwind.config.ts    # Brand color tokens (#0B1B3A, #22E58B, #2F80FF)
│   ├── package.json
│   ├── .env.local.example
│   └── .env.local
│
└── README.md                 # Project roadmap, setup guide & API documentation
```

---

## 🎨 Brand Identity

- **Primary Colors**:
  - Deep Navy: `#0B1B3A` (Trustworthy, sleek automotive darkness)
  - Electric Green: `#22E58B` (High-voltage sustainable energy accent)
  - Accent Blue: `#2F80FF` (Modern digital technology highlight)
  - Pure White & Soft Gray: `#FFFFFF`, `#F8FAFC`
- **Typography**: Inter / Poppins clean sans-serif
- **Location Default**: Hyderabad, Telangana, India (₹ INR)
- **Primary Pickup Hubs**:
  1. Hitec City Cyber Towers Hub
  2. Gachibowli Financial District Hub
  3. Madhapur Metro Station Hub
  4. Banjara Hills Road No. 12 Hub
  5. Secunderabad Clock Tower Hub
  6. Kukatpally KPHB Colony Hub

---

## 🚀 Quick Start Guide

### 1. Backend Setup
```bash
cd backend
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
Swagger API Documentation is available at: `http://localhost:8000/api/docs/`

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:3000` in your browser.
