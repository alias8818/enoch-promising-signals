# Signed Claim System with Evidence Strength Markers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-claim-system-with-evidence-strength-markers-86e8ed094d7e`
Run ID: `signed-claim-system-with-evidence-strength-markers-86e8ed094d7e-20260628T164810515669+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/deb7aa3d971c

## What looked useful

The bounded harness shows that signatures alone plus explicit marker policy create machine-checkable auditability that an unsigned text-and-marker baseline lacks; the baseline accepted all 421 invalid cases while the signed system rejected all invalid cases.

## Boundaries and scale limits

Synthetic/proxy cases only; no real agent traces, no blind human audit, no live LLM claim extraction, no distributed key-management test, and no colluding-signer adversary.

## Claim scope

In a deterministic synthetic fixture of 512 signed or invalid claim cases, canonical signed claim envelopes plus evidence-strength policy checks rejected tampered, untrusted, contradicted, missing-evidence, duplicate-source-overstated, and unsupported-strength claims with zero false accepts and zero false rejects.

## Why it stopped

Proxy-only synthetic mechanism validation is useful but not sufficient for a paper or broad reliability claim.

## Recommended next action

Run a bounded real/replayed agent-trace follow-up where agents emit signed claims from tool logs and blind scoring measures unsupported-claim and false-completion reductions versus unsigned notes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Signed-Claim Auditability Benchmark
- Success threshold: At least 30 percent relative reduction in unsupported accepted claims versus unsigned baseline, no more than 5 percent absolute increase in false rejection of valid claims, and reproducible logs/metrics on a held-out trace set.
- Stop condition: Stop if signed claims fail to reduce unsupported accepted claims by at least 10 percent relative or introduce more than 10 percent absolute false rejection of valid claims on the held-out trace set.

## Evidence references

- Artifact root: `<local-path>/projects/signed-claim-system-with-evidence-strength-markers-86e8ed094d7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
