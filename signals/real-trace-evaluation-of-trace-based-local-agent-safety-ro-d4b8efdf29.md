# Real-Trace Evaluation of Trace-Based Local-Agent Safety Routing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evaluation-of-trace-based-local-agent-safety-ro-d4b8efdf29`
Run ID: `real-trace-evaluation-of-trace-based-local-agent-safety-ro-d4b8efdf29-20260526T160141163792+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Trace-Based Safety Router for Local Agents: enoch://control-plane/projects/trace-based-safety-router-for-local-agents-a37e00547c4a/runs/trace-based-safety-router-for-local-agents-a37e00547c4a-20260526T084501014004+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

Trace context, especially the originating project root, materially changes safety routing on real local-agent traces by identifying broad cross-project/home traversal and writes outside the active project that command-only destructive/network/secret keywords miss.

## Boundaries and scale limits

Local worker traces only; shell command_execution events only; deterministic rule labels rather than independent human labels; router overlaps with the labeling rules; no live enforcement, user-approval UX, adversarial obfuscation, or cross-organization validation.

## Claim scope

On 41,469 real local Enoch/Codex shell-command trace events from this worker, a project-root-aware trace router captured all 2,885 predeclared rule-labeled review-worthy actions with a 6.96% review rate, while a command-keyword baseline captured 31.5%.

## Why it stopped

Mechanism supported on rule-labeled real traces, but this is no-paper evidence because the labels are not independently adjudicated and the router implements the audit rules rather than proving generalization.

## Recommended next action

Run a bounded human-audited shadow-routing follow-up on a stratified held-out trace sample before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-Audited Shadow Routing for Trace-Based Local-Agent Safety
- Success threshold: Human-audited high-risk recall >= 0.95, review rate <= 0.15, at least 100 audited positive events, and no unmitigated severe false negatives.
- Stop condition: Stop if human-audited recall is below 0.90, review rate exceeds 0.25, or severe false negatives cluster around common local-agent workflows.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evaluation-of-trace-based-local-agent-safety-ro-d4b8efdf29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
