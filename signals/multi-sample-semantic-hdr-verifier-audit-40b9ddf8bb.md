# Multi-sample semantic HDR verifier audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-sample-semantic-hdr-verifier-audit-40b9ddf8bb`
Run ID: `multi-sample-semantic-hdr-verifier-audit-40b9ddf8bb-20260520T194602434502+0000`

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

- Parent run decision: Dual-Temperature HDR Inference Oracle — 10-prompt smoke: enoch://control-plane/projects/dual-temperature-hdr-inference-oracle-10-prompt-smoke/runs/dual-temperature-hdr-inference-oracle-10-prompt-smoke-20260520T191532331908+0000
- Parent run decision: 60-prompt dual-temperature HDR confirmation with verifier audit: enoch://control-plane/projects/60-prompt-dual-temperature-hdr-confirmation-with-verifier-6ee2383fd9/runs/60-prompt-dual-temperature-hdr-confirmation-with-verifier-6ee2383fd9-20260520T193552763184+0000

## What looked useful

Multi-sampling independent semantic signatures gave a clear monotonic verifier improvement and beat lexical and token HDR baselines, especially on high-overlap hard negatives, but the result remains mechanism support rather than publication-grade evidence.

## Boundaries and scale limits

Synthetic/local text-pair audit with a handcrafted semantic parser and stochastic hypervector signatures; no real LLM verifier traces, public NLI/STS benchmark labels, human labels, deployed verifier traffic, or HDR image semantics were tested.

## Claim scope

On controlled generated semantic-pair data with known labels, fixed seeds, a lexical baseline, token-only ablation, exact-parser upper bound, and K-sample ablations, independent multi-sample semantic HDR signatures improved binary equivalence verification from K=1 F1 0.7622 to K=15 F1 0.9489 and reduced false accepts from 0.3661 to 0.0714.

## Why it stopped

Moderate local evidence supports the mechanism, but the current evidence is synthetic and handcrafted, so it is insufficient for a paper-ready claim.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same fixed-seed K-sample protocol on a real NLI/STS or LLM-judge trace dataset with false-accept-rate targets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset multi-sample semantic verifier audit
- Success threshold: K=9 or K=15 semantic multi-sampling improves held-out F1 by at least 0.08 over K=1 and reduces false-accept rate by at least 30% relative to lexical and token-only baselines without increasing false rejects above 0.10.
- Stop condition: Stop if K-sample gains are under 0.03 F1 on two fixed-seed real-data runs or if false-accept rate remains above the lexical baseline.

## Evidence references

- Artifact root: `<local-path>/projects/multi-sample-semantic-hdr-verifier-audit-40b9ddf8bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
