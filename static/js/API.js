/// Api fetch

document.addEventListener("DOMContentLoaded", function() {
  const portfolioSection = document.getElementById("portfolio-section");

  // Función para obtener datos del portafolio desde el backend Flask
  async function fetchPortfolioData() {
    try {
      const response = await fetch("/api/portfolio"); // Llama a la API
      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }
      const data = await response.json();
      displayPortfolio(data);
    } catch (error) {
      console.error("Error al obtener los datos:", error);
      portfolioSection.innerHTML = "<p>Error al cargar los proyectos.</p>"; // Mensaje de error en el DOM
    }
  }

  function displayPortfolio(project) {
    i = 1;
    project.forEach(p => {
      const new_project = {
        id: i,
        title: p.name,
        category: "web", // p.category
        image: "https://picsum.photos/id/1/300/200",
        description: p.description,
        github: "https://github.com/moiseStudent/" + p.name
      };
      projects.push(new_project);
      i++;
    });
  }

  // Llama a la función para obtener datos cuando se carga la página
  fetchPortfolioData();
});

let projects = [];
// Datos de los proyectos

/*
 const projects = [{
         id: 1,
         title: "Proyecto Web 1",
         category: "web",
         image: "https://picsum.photos/id/1/300/200",
         description: "Una aplicación web moderna y responsiva",
         github: "https://github.com/user/proyecto-web-1"
     },
     {
         id: 2,
         title: "App Móvil 1",
         category: "mobile",
         image: "https://picsum.photos/id/2/300/200",
         description: "Una app móvil innovadora para iOS y Android",
         github: "https://github.com/user/app-movil-1"
     },
     {
         id: 3,
         title: "Software de Escritorio 1",
         category: "desktop",
         image: "https://picsum.photos/id/3/300/200",
         description: "Una potente herramienta de productividad",
         github: "https://github.com/user/software-escritorio-1"
     },
     {
         id: 4,
         title: "Proyecto Web 2",
         category: "web",
         image: "https://picsum.photos/id/4/300/200",
         description: "Un sitio web de comercio electrónico",
         github: "https://github.com/user/proyecto-web-2"
     },
     {
         id: 5,
         title: "App Móvil 2",
         category: "mobile",
         image: "https://picsum.photos/id/5/300/200",
         description: "Una app de fitness y salud",
         github: "https://github.com/user/app-movil-2"
     },
     {
         id: 6,
         title: "Software de Escritorio 2",
         category: "desktop",
         image: "https://picsum.photos/id/6/300/200",
         description: "Un editor de video avanzado",
         github: "https://github.com/user/software-escritorio-2"
     },

 ];
 */

const itemsPerPage = 6;
let currentPage = 1;
let currentCategory = "all";

function renderProjects(projects) {
  const portfolioGrid = document.querySelector(".portfolio-grid");
  portfolioGrid.innerHTML = "";

  projects.forEach(project => {
    const projectElement = document.createElement("div");
    projectElement.className = "portfolio-item";
    projectElement.innerHTML = `
            <div class="portfolio-item-inner">
                <div class="portfolio-item-front">
                    <img src="${project.image}" alt="${project.title}">
                    <h3>${project.title}</h3>
                </div>
                <div class="portfolio-item-back">
                    <h3>${project.title}</h3>
                    <p>${project.description}</p>
                    <a href="${project.github}" target="_blank">Ver en GitHub</a>
                </div>
            </div>
        `;
    portfolioGrid.appendChild(projectElement);
  });
}

function filterProjects() {
  const filteredProjects =
    currentCategory === "all"
      ? projects
      : projects.filter(project => project.category === currentCategory);

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedProjects = filteredProjects.slice(startIndex, endIndex);

  renderProjects(paginatedProjects);
  renderPagination(filteredProjects.length);
}

function renderPagination(totalItems) {
  const paginationElement = document.querySelector(".pagination");
  const pageCount = Math.ceil(totalItems / itemsPerPage);

  paginationElement.innerHTML = "";
  for (let i = 1; i <= pageCount; i++) {
    const button = document.createElement("button");
    button.textContent = i;
    button.classList.toggle("active", i === currentPage);
    button.addEventListener("click", () => {
      currentPage = i;
      filterProjects();
    });
    paginationElement.appendChild(button);
  }
}

// Event listeners para los botones de categoría
document.querySelectorAll(".category-filter button").forEach(button => {
  button.addEventListener("click", () => {
    currentCategory = button.dataset.category;
    currentPage = 1;
    document
      .querySelector(".category-filter button.active")
      .classList.remove("active");
    button.classList.add("active");
    filterProjects();
  });
});

// Inicializar la página
filterProjects();
