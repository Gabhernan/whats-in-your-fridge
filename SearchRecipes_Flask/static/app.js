// Normalize comma-separated inputs before submit
const form = document.getElementById('quizForm');
if (form) {
  form.addEventListener('submit', (e) => {
    const ingredients = document.getElementById('ingredients');
    const allergies  = document.getElementById('allergies');

    // basic front-end validation
    if (!ingredients.value.trim()) {
      alert('Please enter at least one ingredient (comma-separated).');
      e.preventDefault();
      return;
    }

    // normalize: lowercase, collapse spaces, remove trailing commas
    const normalize = (str) =>
      str.split(',')
         .map(s => s.trim().toLowerCase())
         .filter(Boolean)
         .join(',');

    ingredients.value = normalize(ingredients.value);
    if (allergies) allergies.value = normalize(allergies.value);
  });
}
