# Real-Model RAG Prompt-Injection Test for Provenance-Gated Evidence Ledgers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-model-rag-prompt-injection-test-for-provenance-gated-ccbca6967f`
Run ID: `real-model-rag-prompt-injection-test-for-provenance-gated-ccbca6967f-20260611T081958665731+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-Ledger vs Adversarial Prompt Injection: enoch://control-plane/projects/evidence-ledger-vs-adversarial-prompt-injection-7ed6629c6aa4/runs/evidence-ledger-vs-adversarial-prompt-injection-7ed6629c6aa4-20260611T062948706498+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb94e1342f57

## What looked useful

The tested model ignored injected retrieved-passage instructions and answered from factual passages even under a deliberately unsafe context-obedient positive-control prompt, so this setup cannot demonstrate a gating benefit without first finding a susceptible baseline.

## Boundaries and scale limits

Single small local model, synthetic controlled corpus, scripted retrieval order, eight cases, non-adaptive payloads, CPU-only short run; not a live web RAG or multi-model robustness validation.

## Claim scope

On eight controlled opaque-fact RAG questions using local Qwen/Qwen2.5-0.5B-Instruct, provenance-gated evidence ledgers preserved answer correctness but did not reduce prompt-injection success because the ungated baseline had zero observed injection successes.

## Why it stopped

Tier-1 direct small test completed with an early negative mechanism result: zero baseline injection successes, so provenance gating showed no measurable attack-reduction delta; this is not a full validation.

## Recommended next action

Run a bounded deepen test that first calibrates a susceptible baseline across stronger payloads and at least two additional models, then measures whether provenance gating reduces injection success while preserving answer accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Multi-Model RAG Injection Susceptibility Before Provenance-Gating Delta Test
- Success threshold: Ungated baseline injection success is at least 30% on the calibrated suite and provenance-gated injection success is at least 50% lower with answer correctness at least 80%.
- Stop condition: Stop as negative if no tested baseline reaches 10% injection success after calibrated payload strengthening, or if provenance gating reduces correctness below 80% while not reducing injection success.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-rag-prompt-injection-test-for-provenance-gated-ccbca6967f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
