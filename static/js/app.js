// Fetch app data from the server
fetch('/apps')
    .then(response => response.json())
    .then(apps => {
        const appList = document.querySelector('.app-list');
        apps.forEach(app => {
            const appCard = document.createElement('div');
            appCard.classList.add('app-card');
            appCard.innerHTML = `
                <img src="${app.icon}" alt="${app.name}">
                <h3>${app.name}</h3>
                <p>${app.description}</p>
                <button>Install</button>
            `;
            appList.appendChild(appCard);
        });
    })
    .catch(error => console.error(error));

// Fetch category data from the server
fetch('/categories')
    .then(response => response.json())
    .then(categories => {
        const categoryList = document.querySelector('.category-list');
        categories.forEach(category => {
            const categoryCard = document.createElement('div');
            categoryCard.classList.add('category-card');
            categoryCard.innerHTML = `
                <img src="${category.icon}" alt="${category.name}">
                <h3>${category.name}</h3>
            `;
            categoryList.appendChild(categoryCard);
        });
    })
    .catch(error => console.error(error));