# 🤖 Day 36 — React Router DOM: Agentic AI Anime Navigation System


# 🚀 Project Overview

Welcome to **Day 36** of my React learning journey.

In this project, I learned how to build a **Single Page Application (SPA)** using **React Router DOM**. Instead of loading a new HTML page every time a user clicks a link, React Router updates only the required component, making navigation smooth and fast.

To make learning more engaging, I designed the project around a **creative Agentic AI Anime Universe**, where users can navigate through futuristic AI-powered worlds.

This project demonstrates the core concepts of client-side routing while maintaining clean folder organization and reusable React components.

---

# 📸 Project Theme

## 🌌 Agentic AI Anime

Imagine a futuristic world where intelligent AI agents protect digital civilizations.

Users can travel through different cyber worlds, learn about Agentic AI, and explore AI-powered destinations.

Pages included in this project:

* 🏠 Home
* 🧠 About
* 🌍 Destinations
* 🚫 Custom 404 Page

---

# 🎯 Learning Objectives

By building this project, I learned how to:

* Build a Single Page Application (SPA)
* Install and configure React Router
* Create multiple pages
* Navigate without page reloads
* Create reusable components
* Use nested folder structures
* Handle unknown routes
* Organize React applications professionally

---

# 📂 Folder Structure

```text
frontend-react/
└── day-36/
    ├── src/
    │
    ├── components/
    │   └── Navbar.jsx
    │
    ├── pages/
    │   ├── Home.jsx
    │   ├── About.jsx
    │   ├── Destinations.jsx
    │   └── NotFound.jsx
    │
    ├── App.jsx
    ├── main.jsx
    └── index.css
```

---

# 🛠 Technologies Used

* React 19
* React Router DOM v7
* Vite
* JavaScript (ES6+)
* HTML5
* CSS3

---

# 📚 React Router Concepts Covered

## BrowserRouter

Wraps the entire application and enables client-side routing.

```jsx
<BrowserRouter>
    <App />
</BrowserRouter>
```

---

## Routes

Contains all application routes.

```jsx
<Routes>

</Routes>
```

---

## Route

Maps a URL path to a React component.

```jsx
<Route path="/" element={<Home />} />
```

---

## NavLink

Creates navigation links and automatically applies an active class.

```jsx
<NavLink to="/">
    Home
</NavLink>
```

---

## Link

Navigates without refreshing the page.

```jsx
<Link to="/">
    Back Home
</Link>
```

---

## Wildcard Route

Displays a custom page whenever the URL does not exist.

```jsx
<Route path="*" element={<NotFound />} />
```

---

# 🖥 Pages

## 🏠 Home

The landing page introduces users to the futuristic Agentic AI Anime world.

Features:

* Welcome section
* Mission statement
* AI introduction

---

## 🧠 About

Explains what Agentic AI is and how autonomous AI systems work.

Topics include:

* Reasoning
* Planning
* Memory
* Decision Making
* Tool Usage

---

## 🌍 Destinations

Displays fictional AI-powered anime locations.

Example destinations:

* Neo Tokyo
* Cyber Castle
* AI Academy
* Quantum Forest
* Robot Kingdom
* Galaxy Hub

---

## 🚫 Not Found

Handles invalid URLs gracefully.

Instead of displaying a blank page, users see a custom 404 screen with a button to return home.

---

# ⚙ Installation

Clone the repository.

```bash
git clone <repository-url>
```

Go to the project folder.

```bash
cd frontend-react/day-36
```

Install dependencies.

```bash
npm install
```

Run the development server.

```bash
npm run dev
```

Open your browser.

```
http://localhost:5173
```

---

# 📖 What I Learned

During this project I understood:

* What client-side routing is
* Why SPAs are faster than traditional websites
* Difference between React navigation and HTML navigation
* How BrowserRouter works
* Why React Router improves user experience
* How components can be reused
* Organizing folders for scalability

---

# 🌟 Advantages of React Router

* Faster navigation
* No full page reload
* Better user experience
* Cleaner URL management
* Easy scalability
* Component-based routing
* Supports nested routes
* Supports dynamic routing

---

# 🧠 Key Takeaways

This project helped me understand the foundation of routing in React.

Instead of thinking in terms of HTML pages, React applications are built using components that change dynamically based on the current URL.

This concept is essential before learning advanced topics such as:

* Protected Routes
* Nested Routes
* Route Parameters
* Loaders
* Authentication
* Dashboard Layouts

---

# 🚀 Future Improvements

Possible enhancements include:

* Authentication
* Login & Signup
* Dark/Light Mode
* Route Guards
* Dynamic Anime Details
* Search Functionality
* API Integration
* Loading Spinner
* Framer Motion Animations
* Responsive Mobile Navigation
* Theme Switching
* Agent Dashboard

---

# 📈 Learning Progress

```
React Learning Journey

✅ Components
✅ Props
✅ State
✅ Events
✅ Conditional Rendering
✅ Lists
✅ Forms
✅ Hooks
✅ useEffect
✅ Custom Components
✅ Styling
✅ React Router DOM
⬜ Context API
⬜ Reducer
⬜ Custom Hooks
⬜ API Integration
⬜ Authentication
⬜ Redux
```

---

# 💡 Why React Router?

Traditional websites reload the entire page whenever users navigate.

React Router changes only the required component while keeping the application running.

This makes applications:

* Faster
* Smoother
* More interactive
* More scalable

---

# 🎓 Conclusion

This project marks an important milestone in my React journey.

By learning React Router, I now understand how modern web applications navigate between pages without full page refreshes. This knowledge forms the foundation for building larger applications such as dashboards, e-commerce platforms, AI applications, and SaaS products.

The Agentic AI Anime theme made the learning experience more enjoyable while reinforcing core routing concepts in a practical project.

---

## 👨‍💻 Author

**Saurabh Kumara**

M.Tech (Computer Science Engineering)

Aspiring AI Engineer | Full Stack Developer | Agentic AI Enthusiast

---

## ⭐ If you found this project helpful

Please consider giving the repository a **Star ⭐** and sharing your feedback.

Happy Coding! 🚀


# Next Day

Topics:

- Context API
- createContext
- useContext
- Theme Management

Project:

Theme Switcher Application