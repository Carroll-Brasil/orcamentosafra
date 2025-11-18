import type { Metadata, Viewport } from "next";
import { Inter, Fira_Code } from "next/font/google";
import "./globals.css";
import { cn } from "@/lib/utils";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
});

const firaCode = Fira_Code({
  subsets: ["latin"],
  variable: "--font-mono",
});

export const metadata: Metadata = {
  title: "Mollusk | Automação Inteligente de Processos",
  description: "A Mollusk é automação. Reduza tarefas manuais, elimine erros e acelere a entrega com fluxos de trabalho sob medida para sua empresa.",
  openGraph: {
    title: "Mollusk | Automação Inteligente de Processos",
    description: "A Mollusk é automação. Reduza tarefas manuais, elimine erros e acelere a entrega com fluxos de trabalho sob medida para sua empresa.",
    url: "https://mollusk.com", // Replace with actual URL
    siteName: "Mollusk",
    images: [
      {
        url: "/og-image.png", // Replace with actual OG image path
        width: 1200,
        height: 630,
      },
    ],
    locale: "pt_BR",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Mollusk | Automação Inteligente de Processos",
    description: "A Mollusk é automação. Reduza tarefas manuais, elimine erros e acelere a entrega com fluxos de trabalho sob medida para sua empresa.",
    images: ["/twitter-image.png"], // Replace with actual Twitter image path
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  icons: {
    icon: "/favicon.ico",
    shortcut: "/favicon-16x16.png",
    apple: "/apple-touch-icon.png",
  },
};

export const viewport: Viewport = {
  themeColor: "#0D1117",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body className={cn(
        "min-h-screen bg-background font-sans antialiased overflow-x-hidden",
        inter.variable,
        firaCode.variable
      )}>
        {children}
      </body>
    </html>
  );
}
