# Restaurant Reservation System

This project is a web-based restaurant reservation system designed for both guest and registered users. It allows users to search for available tables, make reservations, and receive confirmations. The system adapts to high-traffic days, supports table combinations, and includes loyalty and no-show features for registered users.

## 🛠 Technologies Used

### Frontend
- React.js
- Tailwind CSS
- Figma (for UI mockups)

### Backend
- Node.js with Express
- TypeScript
- RESTful API structure

### Architecture
- Layered architecture (Presentation, Application, Data, External Services)
- Modular components with clear separation of concerns

### External Services (planned)
- Stripe or equivalent (payment gateway)
- Twilio or email API (notifications)

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-team/reservation-system.git
cd reservation-system
```

### 2. Run the Backend

```bash
cd backend
npm install
npm run dev
```

Runs on http://localhost:3001

### 3. Run the Frontend

```bash
cd frontend
npm install
npm start
```

Runs on http://localhost:3000

> Make sure the backend server is running before submitting a reservation.

## 🧪 Example Input

```json
{
  "name": "Jane Smith",
  "phone": "555-4321",
  "email": "jane@example.com",
  "date": "2025-05-10",
  "time": "19:00",
  "guests": 4
}
```

## ✅ Output

- Form displays confirmation message: `Reservation received!`
- Server console logs submitted reservation
- (Future: Confirmation email/SMS)

## 👥 Team Members & Contributions

| Name          | Role                        |
|---------------|-----------------------------|
| Kyra Smith    | UI/UX design, React setup   |
| Nneoma Kalu   | Backend logic, TypeScript API |
| Kenneth Sam   | Domain logic, architecture  |

---

Thank you for reviewing our project!
