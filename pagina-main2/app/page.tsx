"use client";

import { ShaderBackground } from "@/components/ui/shader-background";
import { NavBar } from "@/components/ui/tubelight-navbar";
import { GooeyText } from "@/components/ui/gooey-text-morphing";
import { PlaceholdersAndVanishInput } from "@/components/ui/placeholders-and-vanish-input";
import { Zap, BadgeCheck, Clock, Home as HomeIcon, Lightbulb, CaseSensitive, Wrench, Book, Mail } from "lucide-react";

const gooeyWords = [
  "automação", "desenvolvimento", "simplicidade", "expertise",
  "integração", "eficiência", "escalabilidade", "confiabilidade",
  "orquestração", "produtividade", "IA aplicada", "resultados"
];

const navItems = [
  { name: "Início", url: "/", icon: HomeIcon },
  { name: "Soluções", url: "/solucoes", icon: Lightbulb },
  { name: "Casos", url: "/casos", icon: CaseSensitive },
  { name: "Como Trabalhamos", url: "/como-trabalhamos", icon: Wrench },
  { name: "Blog", url: "/blog", icon: Book },
  { name: "Contato", url: "/contato", icon: Mail },
];

export default function Home() {
  const handlePromptSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("submitted");
  };

  const handlePromptChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
  };

  return (
    <main className="flex flex-col items-center justify-center">
      <NavBar items={navItems} />
      <ShaderBackground />

      {/* Hero Section */}
      <section className="relative w-full h-screen flex flex-col items-center justify-center text-center px-4">
        <h1 className="text-5xl md:text-7xl font-extralight tracking-tight text-white text-center">
          <span className="block">A Mollusk é</span>
          <div className="mt-6 md:mt-8 flex justify-center">
            <GooeyText
              texts={gooeyWords}
              textClassName="text-4xl md:text-6xl font-extralight tracking-tight"
            />
          </div>
        </h1>
        <p className="mt-8 md:mt-10 text-lg md:text-xl font-light leading-relaxed tracking-tight text-white/75 max-w-2xl">
          Reduza tarefas manuais, elimine erros e acelere a entrega com fluxos de trabalho sob medida para sua empresa.
        </p>
        <div className="mt-12 w-full max-w-2xl">
          <PlaceholdersAndVanishInput
            placeholders={[
              "Como automatizar meu processo de onboarding?",
              "Quero integrar a API do meu CRM com o Slack",
              "Crie um fluxo de trabalho para aprovação de despesas",
            ]}
            onSubmit={handlePromptSubmit}
            onChange={handlePromptChange}
          />
        </div>
      </section>

      {/* Value Proposition Section */}
      <section className="w-full py-20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-extralight tracking-tight text-white">Por que automatizar com a Mollusk?</h2>
          <div className="mt-12 grid md:grid-cols-3 gap-8">
            <div className="flex flex-col items-center p-8 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">
              <Zap className="w-12 h-12 text-cyan-400" />
              <h3 className="mt-4 text-xl font-semibold text-white">Mais Velocidade</h3>
              <p className="mt-2 text-white/75 font-light tracking-tight">Entregue projetos e resultados em dias, não meses.</p>
            </div>
            <div className="flex flex-col items-center p-8 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">
              <BadgeCheck className="w-12 h-12 text-cyan-400" />
              <h3 className="mt-4 text-xl font-semibold text-white">Menos Erros</h3>
              <p className="mt-2 text-white/75 font-light tracking-tight">Elimine falhas humanas em processos críticos.</p>
            </div>
            <div className="flex flex-col items-center p-8 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">
              <Clock className="w-12 h-12 text-cyan-400" />
              <h3 className="mt-4 text-xl font-semibold text-white">Foco no Essencial</h3>
              <p className="mt-2 text-white/75 font-light tracking-tight">Libere sua equipe de tarefas repetitivas e manuais.</p>
            </div>
          </div>
        </div>
      </section>

      {/* How We Work Section */}
      <section className="w-full py-20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-extralight tracking-tight text-white">Nosso Processo em 4 Passos</h2>
          <div className="mt-12 max-w-4xl mx-auto grid md:grid-cols-4 gap-8 text-center">
             <div className="p-6 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">1. Descoberta</div>
             <div className="p-6 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">2. Desenho do Fluxo</div>
             <div className="p-6 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">3. Implementação</div>
             <div className="p-6 bg-neutral-900/80 backdrop-blur-sm border border-white/10 rounded-2xl">4. Medição</div>
          </div>
        </div>
      </section>

      {/* Final CTA Section */}
      <section className="w-full py-20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-extralight tracking-tight text-white">Pronto para começar?</h2>
          <p className="mt-4 text-lg text-neutral-300">Dê o primeiro passo para a transformação digital da sua empresa.</p>
          <div className="mt-8 w-full max-w-2xl mx-auto">
            <PlaceholdersAndVanishInput
              placeholders={[
                "Vamos conversar sobre meu projeto",
                "Agendar uma demonstração",
                "Quero um orçamento",
              ]}
              onSubmit={handlePromptSubmit}
              onChange={handlePromptChange}
            />
          </div>
        </div>
      </section>
    </main>
  );
}

