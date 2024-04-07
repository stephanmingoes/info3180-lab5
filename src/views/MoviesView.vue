<template>
  <div class="container">
    <h1>Movies</h1>
    <div class="row">
      <div class="col-md-6">
        <router-link to="/movies/create" class="btn btn-primary mb-3"
          >Create Movie</router-link
        >
      </div>
    </div>
    <div>
      <!-- create a grid with a card having the movie image, title and description -->

      <div class="row">
        <div class="col-md-4" v-for="movie in movies" :key="movie.id">
          <div class="card mb-3">
            <div>
              <img :src="movie.poster" class="card-img-top" alt="movie.title" />
            </div>

            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">{{ movie.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const movies = ref([]);

onMounted(async () => {
  const res = await fetch("/api/v1/movies");
  const data = await res.json();
  movies.value = data.movies;
  console.log(movies.value);
});
</script>
