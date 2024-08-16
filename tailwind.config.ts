import type { Config } from "tailwindcss";
import { nextui } from "@nextui-org/react";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    fontFamily: {
      // display: ['Inter', 'sans-serif'],
      // body: ['Inter', 'sans-serif'],
      display: ['Noto Sans', 'sans-serif'],
      body: ['Chivo', 'sans-serif']
    },
  },
  daisyui: {
    themes: ['light', 'dark']
  },
  darkMode: 'selector',
  plugins: [nextui(), require('daisyui')],
};
export default config;