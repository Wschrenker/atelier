# Gemini-Gespräch 2/4 — Prinzipien modularer Software

> Gesprächsnotiz zur gemeinsamen Ideenentwicklung. Sie gehört zu den Dateien `geminichatanweisung01.md` bis `geminichatanweisung04.md` und ist keine verbindliche Projektregel.

## Ausgangsfrage

Werner fragte nach den wichtigsten Punkten beim Aufbau eines modularen Softwaresystems und nach Dateien oder Hilfsmitteln, mit denen sich diese Vorgaben umsetzen lassen.

## Fünf Prinzipien

### 1. Klare Schnittstellen und Verträge

Jedes Modul erhält eine explizite Schnittstelle oder API. Andere Teile kommunizieren ausschließlich über diesen Vertrag und greifen nicht direkt auf interne Klassen, Datenstrukturen oder Tabellen zu.

### 2. Hohe Kohäsion und klare Verantwortung

Jedes Modul besitzt eine klar abgegrenzte fachliche Aufgabe. Zusammengehörige Logik bleibt im Modul; fachfremde Logik gehört in einen anderen Baustein.

### 3. Keine zirkulären Abhängigkeiten

Abhängigkeiten sollen gerichtet verlaufen. Wenn direkte Kopplung problematisch wird, kommen Dependency Inversion oder ereignisbasierte Kommunikation als mögliche Werkzeuge infrage.

### 4. Isolierte Testbarkeit und Ersetzbarkeit

Module sollen unabhängig vom Gesamtsystem getestet werden können. Mocks, Stubs oder kleine In-Memory-Ersatzobjekte können externe Abhängigkeiten im Test ersetzen.

### 5. Expliziter Datentransfer statt globalem Zustand

Globale Variablen und gemeinsam veränderte Objekte sollen vermieden werden. Module tauschen Daten über klar definierte, möglichst unveränderliche DTOs oder Event-Payloads aus.

## Genannte Hilfsmittel

### Schnittstellenverträge

Mögliche Formen sind `openapi.yaml`, Protobuf oder Sprach-Interfaces. Sie beschreiben APIs und Datenstrukturen vor der Implementierung.

### Architekturregeln und Linter

Werkzeuge wie ESLint oder ArchUnit können unerlaubte Modulzugriffe und zirkuläre Importe früh erkennen.

```javascript
rules: {
  'no-restricted-imports': ['error', {
    patterns: [{ group: ['../**/internal/*'], message: 'Zugriff auf interne Modulklassen verboten.' }]
  }],
  'import/no-cycle': ['error', { maxDepth: 1 }]
}
```

### Zentrales Wiring

Ein Composition Root oder Dependency-Injection-Container setzt Module und Adapter an einer zentralen Stelle zusammen.

```typescript
container.register<PaymentPort>('PaymentPort', { useClass: StripeAdapter });
container.register(OrderService, { useClass: OrderService });
```

### Event-Schemas und unveränderliche DTOs

Zwischen Modulen werden ausdrücklich beschriebene Datenobjekte übergeben.

```typescript
export class OrderCreatedEvent {
  constructor(
    public readonly orderId: string,
    public readonly totalAmount: number,
    public readonly occurredAt: Date = new Date()
  ) {
    Object.freeze(this);
  }
}
```

### In-Memory-Stubs und Mock-Infrastruktur

Tests können einfache Ersatzspeicher verwenden, statt eine echte Datenbank zu benötigen.

```typescript
export class InMemoryOrderRepository implements OrderRepositoryPort {
  private orders = new Map<string, Order>();
  async save(order: Order): Promise<void> { this.orders.set(order.id, order); }
}
```

### Workspace-Grenzen

Monorepo- oder Workspace-Konfigurationen können Module auch auf Dateisystem- und Build-Ebene trennen.

```yaml
packages:
  - 'packages/core'
  - 'modules/*'
```

## Einordnung für ATELIER

Die Prinzipien sind relevant. Die genannten Enterprise-Werkzeuge sind Beispiele, keine Pflicht. ATELIER setzt die nötigen Teile zunächst schlank mit Python-Datentypen, lokalen Bausteinverträgen, Tests und klaren Ordnergrenzen um.

## Gesprächsreihe

1. [`geminichatanweisung01.md`](geminichatanweisung01.md): gemeinsames Datenmodell
2. **Diese Datei:** Prinzipien modularer Software
3. [`geminichatanweisung03.md`](geminichatanweisung03.md): 3D-Idee und visuelles Patchwork
4. [`geminichatanweisung04.md`](geminichatanweisung04.md): Engineering Context und Repo-Butler
