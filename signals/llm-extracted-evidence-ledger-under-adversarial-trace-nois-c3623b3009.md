# LLM-extracted evidence ledger under adversarial trace noise

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-extracted-evidence-ledger-under-adversarial-trace-nois-c3623b3009`
Run ID: `llm-extracted-evidence-ledger-under-adversarial-trace-nois-c3623b3009-20260608T041211950875+0000`

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

- Parent run decision: Compressed Evidence Ledger for Small CPU Agent Safety: enoch://control-plane/projects/compressed-evidence-ledger-for-small-cpu-agent-safety-2ba50d592d4b/runs/compressed-evidence-ledger-for-small-cpu-agent-safety-2ba50d592d4b-20260607T223002730597+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd8255f1ed89

## What looked useful

Source-grounded ledger prompting met the Tier 1 threshold: claim F1 1.0, evidence exact rate 1.0, hallucinated evidence IDs 0, and adopted adversarial-noise claims 0 across 24 claims.

## Boundaries and scale limits

Single live model pass; synthetic short cases; fixed claim IDs; explicit evidence snippets; deterministic scorer; no randomized held-out generation, cross-model replication, long-context stress test, adaptive prompt injection, or human semantic audit.

## Claim scope

In 8 short controlled source-plus-adversarial-trace cases with explicit evidence IDs and 24 total gold claims, a live Codex extractor produced complete source-grounded evidence ledgers with exact citations and no detected adoption of factual trace noise.

## Why it stopped

Tier 1 direct test succeeded as a useful mechanism signal, but the evidence is small, synthetic, and single-model, so this run closes as no-paper rather than paper-positive.

## Recommended next action

Run a bounded randomized deepen test with at least 50 generated cases, held-out gold labels, source-only and trace-only baselines, and two independently callable model extractors before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized multi-model evidence ledger robustness under adversarial trace noise
- Success threshold: Source-grounded ledger extraction must achieve claim F1 >= 0.90, exact evidence-ID rate >= 0.95, hallucinated evidence IDs <= 1 percent of predicted citations, and at least 50 percent lower adopted-noise rate than trace-only or ungrounded baselines.
- Stop condition: Stop as negative if source-grounded extraction falls below claim F1 0.85 or exact evidence-ID rate 0.90, or if adopted-noise rate is not at least 25 percent lower than trace-only or ungrounded baselines.

## Evidence references

- Artifact root: `<local-path>/projects/llm-extracted-evidence-ledger-under-adversarial-trace-nois-c3623b3009`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
