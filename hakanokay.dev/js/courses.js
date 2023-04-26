const DATA = [
  {
    id: 1,
    level: 1,
    name: 'Computer Essentials',
    desc: 'The essentials of computer software, hardware, and laptop management form the foundation for building further technical programming skills. Learn to configure your laptop environment, basic PC and troubleshoot problems. Students create backups, install virus protection, and manage files through a basic understanding of the Windows Operating System. Students also install and configure the Windows Operating System, and a virtual machine environment and explore computer organization including basic numerical systems, functional hardware and software components needed to run programs',
    grade:
      '<span class="badge rounded-pill text-bg-success course-badge">A+</span>',
    logo: '<i class="fa-solid me-2 fa-computer"></i>'
  },
  {
    id: 2,
    level: 1,
    name: 'Introduction to Computer Programming',
    desc: 'Possessing the fundamentals of logic, problem-solving and programming language structure provides a solid foundation for further study in the field. Students develop introductory knowledge of computer programming with emphasis on problem analysis and design, using algorithms, pseudocode, flowcharts, UML Class Diagrams and testing, with the Java programming language used as a means to implement problem solution designs. Through an introduction to the Java programming language students use sequential structures, selection structures, repetition structures, variables, constants, methods, constructors, one-dimensional arrays, object-oriented programming, classes, objects, abstraction, encapsulation, inputs, outputs, coding conventions and documentation. Theory is reinforced with application by means of practical laboratory assessments.',
    grade:
      '<span class="badge rounded-pill text-bg-success course-badge">A+</span>',
    logo: '<i class="fa-solid me-2 fa-code"></i>'
  },
  {
    id: 3,
    level: 1,
    name: 'Introduction to Database',
    desc: 'Databases are used to store data and are a core component of many information technology systems. Students learn the fundamentals of relational databases design using Entity Relation Diagrams (ERDs), and use Structured Query Language (SQL) to create, modify and query a database. Students design and create databases that are maintainable, secure and adaptable to change in business requirements, using normalization. Students become familiar with the functions of a Database Management System (DBMS) and its components in comparison with legacy systems and alternative information storage mechanisms.',
    grade:
      '<span class="badge rounded-pill text-bg-success course-badge">A+</span>',
    logo: '<i class="fa-solid me-2 fa-database"></i>'
  },
  {
    id: 4,
    level: 1,
    name: 'Achieving Success in Changing Environments',
    desc: 'Rapid changes in technology have created personal and employment choices that challenge each of us to find our place as contributing citizens in the emerging society. Life in the 21st century presents significant opportunities, but it also creates potential hazards and ethical problems that demand responsible solutions. Students explore the possibilities ahead, assess their own aptitudes and strengths, and apply critical thinking and decision-making tools to help resolve some of the important issues in our complex society with its competing interests.',
    grade:
      '<span class="badge rounded-pill text-bg-success course-badge">A+</span>',
    logo: '<i class="fa-solid me-2 fa-thumbs-up"></i>'
  },
  {
    id: 5,
    level: 1,
    name: 'Communications I',
    desc: 'Communication remains an essential skill sought by employers, regardless of discipline or field of study. Using a practical, vocation-oriented approach, students focus on meeting the requirements of effective communication. Through a combination of lectures, exercises, and independent learning, students practise writing, speaking, reading, listening, locating and documenting information and using technology to communicate professionally. Students develop and strengthen communication skills that contribute to success in both educational and workplace environments.',
    grade:
      '<span class="badge rounded-pill text-bg-success course-badge">A</span>',
    logo: '<i class="fa-regular me-2 fa-comment"></i>'
  },
  {
    id: 6,
    level: 1,
    name: 'Technical Mathematics for Computer Science',
    desc: 'The study of algebraic and transcendental functions is an essential prerequisite to Calculus. Students manipulate algebraic expressions, solve algebraic equations and linear systems and learn the properties of and graph algebraic and transcendental functions. Students investigate computer number systems in addition to Boolean algebra and logic to help solve problems involving computer systems. Students also study the addition and subtraction of vectors using vector components. Delivered in a modular format, this course is equivalent to the completion of all of the following math modules MAT8100 - A, B, C, D, E, F, and L.',
    grade:
      '<span class="badge rounded-pill text-bg-success course-badge">A+</span>',
    logo: '<i class="fa-solid me-2 fa-square-root-variable"></i>'
  },
  {
    id: 7,
    level: 2,
    name: 'Database Systems',
    desc: "Database systems can automate data processing tasks as well as tie into the security of information technology systems. Students acquire practical experience using market-leading object-relational database management systems like Oracle and MySQL. Students obtain hands-on experience with advanced engineering modeling tools along with SQL, SQL scripts and programming with Oracle's PL/SQL blocks. Database concepts covered include advanced SQL, case structures, rollup and cube operations, metadata manipulation, data storage and retrieval, security and transaction control and data warehousing",
    grade:
      '<span class="badge rounded-pill text-bg-secondary course-badge">⌛</span>',
    logo: '<i class="fa-solid me-2 fa-server"></i>'
  },
  {
    id: 8,
    level: 2,
    name: 'Operating System Fundamentals (GNU/Linux)',
    desc: 'Operating systems form the backbone of information technology systems coordinating the interaction between hardware and software. Students explore the basic concepts and components of Operating Systems (OS), and how they function and interact with hardware and software components. Students examine the details of operating system structures, process management, storage management, installation, configuration, and administration both in theory and through practical assignments based on the GNU/Linux operating system. Lab work is designed to implement the theory by developing skills using the powerful GNU/Linux command-line tools and utilities.',
    grade:
      '<span class="badge rounded-pill text-bg-secondary course-badge">⌛</span>',
    logo: '<i class="fa-brands me-2 fa-linux"></i>'
  },
  {
    id: 9,
    level: 2,
    name: 'Object Oriented Programming (Java)',
    desc: 'Working in the field of information technology as a programmer requires a firm understanding of Object-Oriented Programming (OOP) concepts. Students explore object-oriented programming methodology using the Java programming language. Object oriented concepts, such as encapsulation, inheritance, abstraction and polymorphism are covered and reinforced with practical applications. Students explore the basics of data structures and algorithms as well as basic Graphical User Interface (GUI) programming.',
    grade:
      '<span class="badge rounded-pill text-bg-secondary course-badge">⌛</span>',
    logo: '<i class="fa-brands me-2 fa-java"></i>'
  },
  {
    id: 10,
    level: 2,
    name: 'Web Programming',
    desc: 'The World Wide Web (WWW) has become an integrated part of everyday life. Students develop basic skills of web programming, website design and implementation. JavaScript, HTML5, and PHP are used to explore web-based solutions to problems of increasing interactivity and complexity. Lectures are reinforced by practical assignments that encourage students to construct and maintain their own websites.',
    grade:
      '<span class="badge rounded-pill text-bg-secondary course-badge">⌛</span>',
    logo: '<i class="fa-brands me-2 fa-square-js"></i>'
  },
  {
    id: 11,
    level: 2,
    name: 'Technical Communication for Engineering Technologies',
    desc: 'The ability to communicate effectively in a technically-oriented interdisciplinary workplace is a foundational skill in an innovation-driven economy. Students are exposed to exercises and assignments designed to foster independent and collaborative critical thinking, research, writing, visual communication and presentation skills related to technical topics.',
    grade:
      '<span class="badge rounded-pill text-bg-secondary course-badge">⌛</span>',
    logo: '<i class="fa-solid me-2 fa-newspaper"></i>'
  },
  {
    id: 12,
    level: 2,
    name: 'Cooperative Education Readiness',
    desc: 'Students are guided through a series of activities that prepare them to conduct a professional job search and succeed in the workplace. Through a detailed orientation students learn the cooperative education program policies and procedures related to searching and securing a work term opportunity. Students identify their strengths and transferable skills and participate in workshop-style sessions that focus on cover letter and resume development, interview techniques and job search strategies. Students learn how to navigate a web-based resource centre, which is used to post employment and cooperative education job opportunities. Students reflect on workplace success, ethics and responsibilities.',
    grade:
      '<span class="badge rounded-pill text-bg-secondary course-badge">⌛</span>',
    logo: '<i class="fa-solid me-2 fa-briefcase"></i>'
  }
]
function display (e) {
  if ((clearList(), e.length === 0)) {
    document.getElementById('expand-courses').innerHTML =
      '<a href="#" class="list-group-item list-group-item-action inactive-link" aria-current="true"><div class="d-flex justify-content-between"><h5 id="course-list-item" data-custom-value="0" class="mb-2 course-title">No Results Found</h5></div><p class="mb-1 course-desc">Please try another keyword.</p></a>'
  } else {
    for (let t = 0; t < e.length; t++) {
      document.getElementById(
        'expand-courses'
      ).innerHTML += `\n      <a href="#" class="list-group-item list-group-item-action inactive-link" aria-current="true"><div class="d-flex justify-content-between"><h5 id="course-list-item" data-custom-value="${e[t].id}" class="mb-1 course-title">${e[t].logo}${e[t].name}<span class="course-level">(Level: ${e[t].level})</span></h5>${e[t].grade}</div><p class="mb-1 course-desc">${e[t].desc}</p></a>`
    }
  }
}
function clearList () {
  document.getElementById('expand-courses').innerHTML = ''
}
function getCurrentDisplay () {
  const e = document.querySelectorAll('#course-list-item')
  const t = []
  for (let a = 0; a < e.length; a++) t.push(e[a].dataset.customValue)
  return DATA.filter((e) => t.includes(e.id.toString()))
}
function getInput () {
  return document.getElementById('search-text').value.toLowerCase().trim()
}
function filterBySearch (e) {
  return DATA.filter(
    (t) => t.name.toLowerCase().includes(e) || t.desc.toLowerCase().includes(e)
  )
}
function sortByLevelAsc (e) {
  return e.sort((e, t) => (e.level > t.level ? -1 : 1))
}
function sortByLevelDesc (e) {
  return e.sort((e, t) => (e.level > t.level ? 1 : -1))
}
function sortDisplay (e) {
  document.getElementById('expand-courses').classList.contains('asc')
    ? (display(sortByLevelDesc(e)),
      document.getElementById('expand-courses').classList.remove('asc'),
      document.getElementById('expand-courses').classList.add('desc'))
    : document.getElementById('expand-courses').classList.contains('desc')
      ? (display(sortByLevelAsc(e)),
        document.getElementById('expand-courses').classList.remove('desc'),
        document.getElementById('expand-courses').classList.add('asc'))
      : (display(sortByLevelAsc(e)),
        document.getElementById('expand-courses').classList.add('asc'))
}
function filterByLevel (e, t) {
  return e.filter((e) => e.level == t)
}
function handleKeyPress (e) {
  e.key === 'Enter' &&
    (display(filterBySearch(getInput())), e.preventDefault())
}
function handleClick (e) {
  display(filterBySearch(getInput())), e.preventDefault()
}
function handleSort (e) {
  sortDisplay(getCurrentDisplay()), e.preventDefault()
}
function handleFilter (e, t) {
  display(filterByLevel(getCurrentDisplay(), t)), e.preventDefault()
}
function handleReset (e) {
  clearList(), display(DATA), e.preventDefault()
}
function main () {
  display(DATA),
  document.addEventListener('keypress', (e) => handleKeyPress(e)),
  document
    .getElementById('button-submit')
    .addEventListener('click', (e) => handleClick(e)),
  document
    .getElementById('button-sort')
    .addEventListener('click', (e) => handleSort(e)),
  document.querySelectorAll('#level-list li a').forEach((e) => {
    e.addEventListener('click', (t) => {
      handleFilter(t, e.getAttribute('data-custom-value'))
    })
  }),
  document
    .getElementById('button-reset')
    .addEventListener('click', (e) => handleReset(e))
}
DATA.sort((e, t) => (e.name > t.name ? 1 : -1)), main()
