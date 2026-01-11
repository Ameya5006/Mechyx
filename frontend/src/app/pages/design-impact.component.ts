import { Component } from "@angular/core";

@Component({
  selector: "app-design-impact",
  standalone: true,
  template: `
    <section class="page">
      <h2>Design Impact Simulator</h2>
      <p>Link recurring issues to components, BOM changes, and design owners.</p>
      <div class="card">
        <h3>Simulation Insight</h3>
        <p>Updated suspension bushing reduces warranty claims by ~22%.</p>
      </div>
    </section>
  `,
})
export class DesignImpactComponent {}
