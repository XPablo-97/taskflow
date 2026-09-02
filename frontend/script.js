const API_URL = "http://localhost:8000";

async function loadTasks() {
  const response = await fetch(`${API_URL}/tasks`);
  const tasks = await response.json();

  const list = document.getElementById("task-list");
  list.innerHTML = "";

  tasks.forEach((task) => {
        const item = document.createElement("li");
    if (task.status === "done") {
      item.classList.add("done");
    }
    item.textContent = `${task.title} — ${task.status} `;

    if (task.status === "pending") {
      const completeButton = document.createElement("button");
      completeButton.textContent = "Completar";
      completeButton.dataset.taskId = task.id;
      completeButton.classList.add("complete-btn");
      item.appendChild(completeButton);
    }

    list.appendChild(item);
  });
}

loadTasks();

const form = document.getElementById("task-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const titleInput = document.getElementById("task-title");
  const title = titleInput.value;

  await fetch(`${API_URL}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });

  titleInput.value = "";
  loadTasks();
});

const list = document.getElementById("task-list");

list.addEventListener("click", async (event) => {
  if (event.target.classList.contains("complete-btn")) {
    const taskId = event.target.dataset.taskId;
    await fetch(`${API_URL}/tasks/${taskId}/complete`, { method: "POST" });
    loadTasks();
  }
});

