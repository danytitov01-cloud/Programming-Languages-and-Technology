const button = document.querySelector("#load");
const status = document.querySelector("#status");
const results = document.querySelector("#results");

button.addEventListener("click", loadPosts);

async function loadPosts() {
    button.disabled = true;
    status.textContent = "Загрузка...";
    results.replaceChildren();

    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/posts?_limit=10"
        );

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const posts = await response.json();

        posts.forEach(post => {
            const item = document.createElement("li");
            item.textContent = `ID: ${post.id} — ${post.title}`;
            results.appendChild(item);
        });

        status.textContent = `Загружено публикаций: ${posts.length}`;
    } catch (error) {
        status.textContent = "Ошибка загрузки: " + error.message;
    } finally {
        button.disabled = false;
    }
}