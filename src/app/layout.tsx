import type { Metadata } from "next";
import { Noto_Sans, Chivo } from "next/font/google";
import "./globals.css";
import { NextUIProvider } from "@nextui-org/react";
import DarkModeWrapper from "@/components/DarkModeWrapper";

const inter = Noto_Sans({ subsets: ["latin"] });
const timesNewRoman = Chivo({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "M",
  description: "m",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${timesNewRoman.className}`}><NextUIProvider><DarkModeWrapper>{children}</DarkModeWrapper></NextUIProvider></body>
    </html>
  );
}