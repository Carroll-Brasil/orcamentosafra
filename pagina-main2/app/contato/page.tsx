"use client";

import { useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { NavBar } from "@/components/ui/tubelight-navbar";
import { Home as HomeIcon, Lightbulb, CaseSensitive, Wrench, Book, Mail } from "lucide-react";

const navItems = [
  { name: "Início", url: "/", icon: HomeIcon },
  { name: "SoluÃ§Ãµes", url: "/solucoes", icon: Lightbulb },
  { name: "Casos", url: "/casos", icon: CaseSensitive },
  { name: "Como Trabalhamos", url: "/como-trabalhamos", icon: Wrench },
  { name: "Blog", url: "/blog", icon: Book },
  { name: "Contato", url: "/contato", icon: Mail },
];

function ContatoInner() {
  const searchParams = useSearchParams();
  const [brief, setBrief] = useState("");

  useEffect(() => {
    const briefFromQuery = searchParams.get("brief");
    if (briefFromQuery) {
      setBrief(briefFromQuery);
    } else {
      const briefFromStorage = localStorage.getItem("mollusk.leadBrief");
      if (briefFromStorage) {
        setBrief(briefFromStorage);
      }
    }
  }, [searchParams]);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const data = Object.fromEntries(formData.entries());
    console.log("Form submitted:", data);
    alert("Formulário enviado com sucesso!");
  };

  return (
    <main className="container mx-auto px-4 py-24">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-4xl font-bold text-center text-white">Fale Conosco</h1>
        <p className="mt-4 text-lg text-center text-neutral-300">
          Estamos prontos para transformar sua ideia em realidade.
        </p>

        <form onSubmit={handleSubmit} className="mt-12 space-y-6">
          <div className="grid w-full items-center gap-1.5">
            <Label htmlFor="name">Nome</Label>
            <Input type="text" id="name" name="name" placeholder="Seu nome completo" required />
          </div>
          <div className="grid w-full items-center gap-1.5">
            <Label htmlFor="email">Email</Label>
            <Input type="email" id="email" name="email" placeholder="seu.email@exemplo.com" required />
          </div>
          <div className="grid w-full items-center gap-1.5">
            <Label htmlFor="phone">Telefone (Opcional)</Label>
            <Input type="tel" id="phone" name="phone" placeholder="(XX) XXXXX-XXXX" />
          </div>
          <div className="grid w-full items-center gap-1.5">
            <Label htmlFor="message">Sua ideia de automação</Label>
            <Textarea
              id="message"
              name="message"
              placeholder="Descreva o que você precisa automatizar..."
              value={brief}
              onChange={(e) => setBrief(e.target.value)}
              required
              rows={6}
            />
          </div>
          <Button type="submit" className="w-full" size="lg">
            Enviar Mensagem
          </Button>
        </form>
      </div>
    </main>
  );
}

export default function ContatoPage() {
  return (
    <div className="bg-black min-h-screen">
      <NavBar items={navItems} />
      <Suspense fallback={<div className="container mx-auto px-4 py-24 text-center text-neutral-300">Carregando…</div>}>
        <ContatoInner />
      </Suspense>
    </div>
  );
}


