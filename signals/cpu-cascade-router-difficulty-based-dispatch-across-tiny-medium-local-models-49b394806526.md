# CPU cascade router: difficulty-based dispatch across tiny/medium local models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526`
Run ID: `cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526-20260619T053942292708+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a9965c62ab63

## What looked useful

Difficulty-based dispatch can be near-oracle on a controlled task family: cascade accuracy 1.0000, all-tiny accuracy 0.4409, all-medium accuracy 1.0000, random same-rate accuracy 0.7689, cascade medium-call rate 0.5658 versus oracle 0.5591.

## Boundaries and scale limits

Proxy-only evidence: no neural tiny/medium local language models, no natural-language benchmark, no tokenizer/model-loading overhead, no batching/server effects, and no broad robustness sweep.

## Claim scope

On a 3,000-task synthetic arithmetic benchmark with symbolic local tiny/medium CPU solvers, a difficulty/confidence cascade matched all-medium accuracy on the 2,250-task test split while routing 56.6% of tasks to medium and reducing mean latency by 19.2% versus all-medium.

## Why it stopped

No-paper closure because the result is a bounded synthetic proxy, not direct evidence for real tiny/medium local models.

## Recommended next action

Run a direct local-model deepen test using actual tiny and medium CPU language models on answer-keyed natural-language tasks with the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local-model cascade routing on answer-keyed natural-language tasks
- Success threshold: Cascade reaches at least 95% of all-medium accuracy and reduces medium calls by at least 25% versus all-medium, while beating random same-rate dispatch by at least 10 percentage points accuracy.
- Stop condition: Stop as negative if cascade accuracy falls below 90% of all-medium accuracy or medium-call reduction is below 15% after calibrated routing.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
