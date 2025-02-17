import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  // ✅ 루트 경로 명시 (frontend 폴더가 Vite 루트라면 './' 유지)
  root: './',

  base: '/', 
  publicDir: path.resolve(__dirname, './public'),
  plugins: [react()],

  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
    extensions: ['.js', '.jsx', '.css'],
  },

  server: {
    host: true,
    port: 5173,
    strictPort: true,
    open: true, // 브라우저 자동 열기
  },

  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    manifest: true,
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].[hash].js',
        chunkFileNames: 'assets/[name].[hash].js',
        assetFileNames: 'assets/[name].[hash].[ext]',
      },
    },
  },

  cacheDir: path.resolve(__dirname, '.vite-cache'), // 캐시 폴더 경로 명시
});
