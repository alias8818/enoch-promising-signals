# Real tiny-agent trace validation of structured evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-agent-trace-validation-of-structured-evidence-le-3c7035a466`
Run ID: `real-tiny-agent-trace-validation-of-structured-evidence-le-3c7035a466-20260530T085223476385+0000`

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

- Parent run decision: Structured evidence ledger for tiny agent tool reliability: enoch://control-plane/projects/structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864/runs/structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864-20260530T034943513104+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba852333a41c

## What looked useful

On 250 clean and 250 corrupted real tiny-agent traces, the full structured ledger validator achieved precision 1.00, recall 1.00, F1 1.00, and false-positive rate 0.00. The id-only ledger ablation had recall 0.80 because it missed tampered-hash corruptions, supporting the hash-binding mechanism. The transcript-only baseline had F1 0.00.

## Boundaries and scale limits

Toy deterministic tasks only; synthetic corruptions; weak transcript baseline; no LLM-written traces, natural-language ambiguity, multi-tool workflows, adversarial ledger-preserving attacks, or human-labeled real trace corpus.

## Claim scope

In a controlled deterministic tiny-agent arithmetic environment, structured evidence ledgers with observation ids, hashes, temporal checks, citation coverage, and recomputation detected all tested clean-vs-corrupt trace cases and outperformed an unstructured transcript plausibility baseline.

## Why it stopped

Tier 1 controlled direct test passed, but evidence remains toy-scale and no-paper; closure is useful signal rather than publication readiness.

## Recommended next action

Run a bounded deepen follow-up on real tiny LLM/tool-agent traces with oracle-labeled corruptions and a stronger transcript or LLM-judge baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate structured evidence ledgers on real tiny LLM/tool-agent traces
- Success threshold: Structured ledger validator recall >= 0.90, false-positive rate <= 0.05, and F1 at least 0.15 above the strongest non-ledger baseline on oracle-labeled traces.
- Stop condition: Stop as negative if recall is below 0.80, false-positive rate exceeds 0.10, or gains over the strongest baseline are under 0.05 after the labeled trace set is complete.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-agent-trace-validation-of-structured-evidence-le-3c7035a466`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
