# Class Finder

**Class Finder** is a simple and interactive web application designed to help users find available classrooms based on the day and time. By leveraging a predefined JSON file with class schedules, the app ensures accurate and quick results.

---

## Features

- **Easy to Use**: Select a day and time to instantly check room availability.
- **Dynamic Updates**: Fetches schedules from a JSON file for real-time checks.
- **Predefined Room List**: Compares schedules against a list of all rooms.
- **Error Handling**: Provides clear feedback when rooms are unavailable or if an error occurs.
- **Responsive Design**: Ensures compatibility with various devices and screen sizes.

---

## Demo

(*Add a live link if hosted, e.g., GitHub Pages or Vercel.*)  
[Live Demo](https://room-finder-two.vercel.app/)

---

## Installation and Setup

Follow these steps to run the project locally:

1. **Clone the Repository**:
   
   git clone https://github.com/Hasanul-Banna-Himel/class-finder.git
   cd class-finder
   

2. **Prepare the JSON File**:
   - Ensure you have a `output.json` file containing the schedule in the following format:
     ```json
     [
         {
             "classDay1": "Sunday",
             "classDay2": "Tuesday",
             "classTime": "09:30 AM-10:50 AM",
             "roomNumber": "08F-20C"
         },
         {
             "classDay1": "Monday",
             "classDay2": "Wednesday",
             "classTime": "11:00 AM-12:20 PM",
             "roomNumber": "07A-07C"
         }
     ]
     ```
   - Place the `output.json` file in the root directory.

3. **Run Locally**:
   - Open the `index.html` file in your browser.
   - To handle fetch requests locally, serve the project using a local server:
     ```bash
     # Using Python (Python 3.x required)
     python -m http.server
     ```
     Open `http://localhost:8000` in your browser.

---

## Usage

1. Select a **Day** and **Time** from the dropdown menus.
2. Click the **Check Available Rooms** button.
3. View the results:
   - If rooms are available, they will be listed.
   - If no rooms are available, an appropriate message will be displayed.

---

## Project Structure


class-finder/
│
├── index.html          # Main HTML file
├── styles.css          # Styling for the app
├── script.js           # Core JavaScript functionality
├── output.json         # Sample schedule data
├── README.md           # Project documentation


---

## Technologies Used

- **HTML5**: For structuring the web application.
- **CSS3**: For styling and layout design.
- **JavaScript (ES6)**: For dynamic functionality and interaction.
- **JSON**: To store and fetch the class schedule data.

---

## Future Enhancements

- **Search Feature**: Allow users to search for specific rooms.
- **Room Booking**: Add functionality to reserve available rooms.
- **Real-Time Backend**: Integrate a backend to manage real-time room availability.
- **Enhanced Mobile Compatibility**: Further optimize the interface for mobile devices.

---

## Sample JSON Format

The `output.json` file should follow this structure:

```json
[
    {
        "classDay1": "Sunday",
        "classDay2": "Tuesday",
        "classTime": "09:30 AM-10:50 AM",
        "roomNumber": "08F-20C"
    },
    {
        "classDay1": "Monday",
        "classDay2": "Wednesday",
        "classTime": "11:00 AM-12:20 PM",
        "roomNumber": "07A-07C"
    }
]
```

---

## Contribution

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Hasanul Banna Himel**  
- GitHub: [Hasanul-Banna-Himel](https://github.com/Hasanul-Banna-Himel)  
- Email: (*hasanulbannahimel2003@gmail.com*)

---
```
