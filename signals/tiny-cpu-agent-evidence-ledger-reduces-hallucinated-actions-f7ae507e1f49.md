# Tiny CPU Agent Evidence Ledger Reduces Hallucinated Actions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-cpu-agent-evidence-ledger-reduces-hallucinated-actions-f7ae507e1f49`
Run ID: `tiny-cpu-agent-evidence-ledger-reduces-hallucinated-actions-f7ae507e1f49-20260607T070235512360+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/af1f0231b993

## What looked useful

The run provides a reproducible harness and metrics for defining hallucinated actions as precondition/evidence mismatches and shows that executor-side evidence gating can eliminate that error class in a tiny controlled setting.

## Boundaries and scale limits

Synthetic symbolic benchmark only; no real LLM policy, no natural-language evidence extraction, no production tool schemas, no latency/cost study, and no adversarial or multi-turn user interaction.

## Claim scope

In a deterministic tiny CPU tool-agent simulation with explicit action preconditions, an evidence-ledger gate reduced unsupported action executions from 33.46%-84.88% of baseline episodes to 0% across three noisy-policy settings, without reducing task success.

## Why it stopped

No-paper closure: this is useful mechanistic evidence from a synthetic proxy, not direct publication-grade validation on real LLM agents.

## Recommended next action

Run a bounded deepen test with a real LLM or local language-model policy, comparing baseline, record-only ledger, and ledger-gated execution on natural-language tool-use tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate evidence-ledger gating on real LLM tool-call traces
- Success threshold: At least 50% relative reduction in unsupported tool-call rate versus baseline and record-only ledger controls, with task success no more than 5 percentage points below baseline.
- Stop condition: Stop if ledger-gated execution fails to reduce unsupported tool calls by 25% relative, or if task success drops by more than 10 percentage points in a 100-task pilot.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-agent-evidence-ledger-reduces-hallucinated-actions-f7ae507e1f49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
