import { Component } from "@angular/core";

@Component({
  selector: "app-issue-atlas",
  standalone: true,
  template: `
    <section class="page">
      <h2>Issue Atlas</h2>
      <p>Map defects across manufacturing, service, and supplier touchpoints.</p>
      <div class="card">
        <h3>Top Cluster: Steering Column</h3>
        <p>34 reports linked to alignment drift in cold climates.</p>
      </div>
    </section>
  `,
})
export class IssueAtlasComponent {}
