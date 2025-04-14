import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // 👈 allows access from outside the container
    port: 5173, // optional but good to make it explicit
  },
})
