const button = document.querySelector("#load");
const status = document.querySelector("#status");
const summary = document.querySelector("#summary");
const results = document.querySelector("#results");

button.addEventListener("click", loadData);

async function loadData() {
    button.disabled = true;
    status.textContent = "Загрузка данных...";
    summary.replaceChildren();
    results.replaceChildren();

    try {
        // Загружаем пользователей и публикации одновременно
        const [usersResponse, postsResponse] = await Promise.all([
            fetch("https://jsonplaceholder.typicode.com/users"),
            fetch("https://jsonplaceholder.typicode.com/posts")
        ]);

        if (!usersResponse.ok || !postsResponse.ok) {
            throw new Error("Ошибка HTTP при загрузке данных");
        }

        // Преобразуем ответы в JSON
        const [users, posts] = await Promise.all([
            usersResponse.json(),
            postsResponse.json()
        ]);

        // Считаем количество публикаций каждого пользователя
        const counts = new Map();

        posts.forEach(post => {
            const currentCount = counts.get(post.userId) || 0;
            counts.set(post.userId, currentCount + 1);
        });

        // Показываем общую статистику
        addSummary(`Пользователей: ${users.length}`);
        addSummary(`Публикаций: ${posts.length}`);

        // Создаём карточки пользователей
        users.forEach(user => {
            const card = document.createElement("article");
            card.className = "card";

            const title = document.createElement("h3");
            title.textContent = user.name;

            const email = document.createElement("p");
            email.textContent = `Email: ${user.email}`;

            const count = document.createElement("p");
            count.textContent =
                `Количество публикаций: ${counts.get(user.id) || 0}`;

            card.append(title, email, count);
            results.appendChild(card);
        });

        status.textContent = "Данные успешно загружены.";
    } catch (error) {
        status.textContent = "Ошибка загрузки: " + error.message;
    } finally {
        button.disabled = false;
    }
}

function addSummary(text) {
    const element = document.createElement("div");
    element.className = "stat";
    element.textContent = text;
    summary.appendChild(element);
}