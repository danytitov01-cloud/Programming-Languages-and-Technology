const button = document.querySelector("#load");
const search = document.querySelector("#search");
const status = document.querySelector("#status");
const results = document.querySelector("#results");

let allPosts = [];

button.addEventListener("click", loadPosts);
search.addEventListener("input", filterPosts);

async function loadPosts() {
    button.disabled = true;
    search.disabled = true;
    status.textContent = "Загрузка публикаций...";
    results.replaceChildren();

    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/posts"
        );

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        allPosts = await response.json();

        search.disabled = false;
        filterPosts();
    } catch (error) {
        allPosts = [];
        status.textContent = "Ошибка загрузки: " + error.message;
    } finally {
        button.disabled = false;
    }
}

function filterPosts() {
    const query = search.value.trim().toLowerCase();

    const filteredPosts = allPosts.filter(post =>
        post.title.toLowerCase().includes(query)
    );

    results.replaceChildren();

    filteredPosts.forEach(post => {
        const card = document.createElement("article");
        card.className = "card";

        const title = document.createElement("h3");
        title.textContent = `ID ${post.id}: ${post.title}`;

        const body = document.createElement("p");
        body.textContent = post.body;

        card.append(title, body);
        results.appendChild(card);
    });

    status.textContent =
        `Найдено публикаций: ${filteredPosts.length} из ${allPosts.length}`;
}