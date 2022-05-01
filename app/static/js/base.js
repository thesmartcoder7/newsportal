currentTime = new Date();

date = currentTime.getDate();
year = currentTime.getFullYear();
month = currentTime.getMonth();

months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

document.querySelector(".month").textContent = months[month];
document.querySelector(".date").textContent = date;
document.querySelector(".year").textContent = year;
