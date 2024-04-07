<template>
  <div class="container">
    <h1>Add Movie</h1>
    <div v-if="errors.length > 0" class="alert alert-danger">
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>
    <div v-if="success" class="alert alert-success">{{ success }}</div>
    <form @submit.prevent="saveMovie" id="movieForm">
      <div class="form-group mb-3" enctype="multipart/form-data">
        <label for="title" class="form-label">Movie Title</label>
        <input type="input" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input
          type="file"
          name="poster"
          class="form-control"
          accept="image/*"
        />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Save</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const errors = ref([]);
const success = ref("");
const csfr_token = ref("");
async function saveMovie() {
  const movieForm = document.getElementById("movieForm");
  const form_data = new FormData(movieForm);

  const res = await fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csfr_token.value,
    },
  });

  if (res.status === 400) {
    const data = await res.json();
    errors.value = data.errors;
    return;
  }
  const data = await res.json();
  success.value = data.message;
  errors.value = [];
}

async function getCsrfToken() {
  try {
    const res = await fetch("/api/v1/csrf-token");
    const data = await res.json();
    csfr_token.value = data.csrf_token;
  } catch (error) {
    console.log(error);
  }
}

onMounted(async () => {
  await getCsrfToken();
});
</script>
