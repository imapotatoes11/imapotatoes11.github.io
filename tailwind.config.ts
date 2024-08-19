import type { Config } from "tailwindcss"
import { nextui } from "@nextui-org/react"

const config = {
  darkMode: ["selector"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
    './node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}'
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
        meteor: {
          "0%": { transform: "rotate(250deg) translateX(0) translateY(-10vw)", opacity: "1" }, // 215deg translateX(0)
          "70%": { opacity: "1" },
          "100%": {
            transform: "rotate(250deg) translateX(-100vh) translateY(-10vw)", // 215deg translateX(-500px)
            opacity: "0",
          },
        },
        "border-beam": {
          "100%": {
            "offset-distance": "100%",
          },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
        meteor: "meteor 5s linear infinite",
        "border-beam": "border-beam calc(var(--duration)*1s) infinite linear",
      },
    },
  },
  daisyui: {
    themes: ["light", "dark", "sunset"],
  },
  plugins: [require("tailwindcss-animate"), nextui(), require("daisyui")],
} satisfies Config

export default config