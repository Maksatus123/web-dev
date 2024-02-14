const addButton = document.getElementById("add-task-btn");
const taskInput = document.getElementById("new-task-input");
const taskList = document.getElementById("task-list");

addButton.addEventListener("click", addTask);

function addTask() {
  const taskText = taskInput.value.trim();
  if (taskText === "") {
    alert("Please enter a task!");
    return;
  }

  const listItem = document.createElement("li");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.addEventListener("change", toggleTaskStatus);

  const span = document.createElement("span");
  span.textContent = taskText;
  const deleteButton = document.createElement("img");
  deleteButton.src = "static/img/deleteIcon.svg";
  deleteButton.alt = "Delete";
  deleteButton.classList = "delete-btn";
  deleteButton.addEventListener("click", deleteTask);

  listItem.appendChild(checkbox);
  listItem.appendChild(span);
  listItem.appendChild(deleteButton);

  taskList.appendChild(listItem);
  taskInput.value = "";
}

function toggleTaskStatus(event) {
  const listItem = event.target.parentElement;
  listItem.classList.toggle("completed");
}

function deleteTask(event) {
  const listItem = event.target.parentElement;
  taskList.removeChild(listItem);
}