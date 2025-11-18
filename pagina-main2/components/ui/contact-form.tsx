"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";

export function ContactForm({
  initialBrief,
}: {
  initialBrief: string;
}) {
  const [brief, setBrief] = useState(initialBrief);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const data = Object.fromEntries(formData.entries());
    console.log("Form submitted:", data);
    alert("Formulário de contato enviado com sucesso!");
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4 space-y-4 text-white/90">
      <div className="grid w-full items-center gap-1.5">
        <Label htmlFor="name" className="font-light text-white/75">Nome</Label>
        <Input type="text" id="name" name="name" placeholder="Seu nome completo" required className="bg-white/5 border-white/10 rounded-lg backdrop-blur-sm" />
      </div>
      <div className="grid w-full items-center gap-1.5">
        <Label htmlFor="email" className="font-light text-white/75">Email</Label>
        <Input type="email" id="email" name="email" placeholder="seu.email@exemplo.com" required className="bg-white/5 border-white/10 rounded-lg backdrop-blur-sm" />
      </div>
      <div className="grid w-full items-center gap-1.5">
        <Label htmlFor="message" className="font-light text-white/75">Sua ideia de automação</Label>
        <Textarea
          id="message"
          name="message"
          placeholder="Descreva o que você precisa automatizar..."
          value={brief}
          onChange={(e) => setBrief(e.target.value)}
          required
          rows={4}
          className="bg-white/5 border-white/10 rounded-lg backdrop-blur-sm"
        />
      </div>
      <Button type="submit" className="w-full bg-white/10 border border-white/10 hover:bg-white/20 text-white font-light rounded-lg backdrop-blur-sm">
        Enviar Contato
      </Button>
    </form>
  );
}
