import { Component } from "@angular/core";

@Component({
  selector: "app-dashboard",
  standalone: true,
  template: `
    <section class="page">
      <h2>Executive Overview</h2>
      <p>
        Track the latest field signals, supplier risk, and high-impact issues in
        one snapshot.
      </p>
      <div class="page-grid">
        <article class="card">
          <h3>Active Issues</h3>
          <p>12 open investigations across drivetrain and electronics.</p>
        </article>
        <article class="card">
          <h3>Supplier Risk</h3>
          <p>3 tier-1 suppliers flagged for delivery variance.</p>
        </article>
        <article class="card">
          <h3>Service Trends</h3>
          <p>Steering vibration reports down 18% after latest fix.</p>
        </article>
      </div>
    </section>
  `,
})
export class DashboardComponent {}
