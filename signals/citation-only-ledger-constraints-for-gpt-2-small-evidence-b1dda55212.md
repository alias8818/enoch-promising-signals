# Citation-only ledger constraints for GPT-2-small evidence agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `citation-only-ledger-constraints-for-gpt-2-small-evidence-b1dda55212`
Run ID: `citation-only-ledger-constraints-for-gpt-2-small-evidence-b1dda55212-20260528T130513255801+0000`

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

- Parent run decision: Evidence-Ledger Constrained Tool Agent on GPT-2-Small: enoch://control-plane/projects/evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757/runs/evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757-20260528T085623358380+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9f6fadd21e81

## What looked useful

Ledger constraints reduced format violations from 1.0 to 0.0 and invalid citation rate from 0.5 to 0.0 on alternating-label prompts. Mean F1 improved from 0.1917 to 0.3111, but absolute evidence-selection quality remained poor.

## Boundaries and scale limits

Synthetic short ledgers only; GPT-2-small without fine-tuning; greedy decoding; no real retrieval benchmark, long-context evidence, human-authored claims, sampling robustness, or calibrated stopping. Exact citation-set accuracy remained 1/60 under constraint.

## Claim scope

In a 60-case controlled synthetic evidence-ledger citation-selection task using the real GPT-2-small checkpoint, a ledger-constrained citation-only decoder eliminated non-citation text and out-of-ledger citation IDs while preserving or improving mean citation F1 relative to unconstrained greedy decoding.

## Why it stopped

No-paper useful signal: the direct Tier 1 mechanism threshold was met for citation validity, but the constrained GPT-2-small agent did not reliably select the correct evidence citations.

## Recommended next action

Run a bounded deepen test with calibrated stopping and a stronger citation scorer or light fine-tuning; stop paper development until exact citation accuracy is materially improved while retaining zero invalid citations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated stopping for ledger-constrained GPT-2-small citation selection
- Success threshold: Ledger-constrained calibrated system has invalid citation rate 0.0, format violation rate 0.0, exact citation-set accuracy >= 0.40, and mean F1 at least 0.10 above unconstrained greedy GPT-2-small.
- Stop condition: Stop if exact citation-set accuracy remains below 0.25 after calibrated stopping or light supervised adaptation, or if any constrained configuration emits out-of-ledger citations.

## Evidence references

- Artifact root: `<local-path>/projects/citation-only-ledger-constraints-for-gpt-2-small-evidence-b1dda55212`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
