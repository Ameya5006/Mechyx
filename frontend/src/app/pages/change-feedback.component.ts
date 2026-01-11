import { Component } from "@angular/core";

@Component({
  selector: "app-change-feedback",
  standalone: true,
  template: `
    <section class="page">
      <h2>Change Feedback Loop</h2>
      <p>Measure how fixes reduce defect rates across the lifecycle.</p>
      <div class="card">
        <h3>Recent Impact</h3>
        <p>Brake wear complaint rate down 14% after rotor update.</p>
      </div>
    </section>
  `,
})
export class ChangeFeedbackComponent {}
