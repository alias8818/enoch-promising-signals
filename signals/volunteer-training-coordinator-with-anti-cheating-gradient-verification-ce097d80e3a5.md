# Volunteer Training Coordinator with Anti-Cheating Gradient Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-training-coordinator-with-anti-cheating-gradient-verification-ce097d80e3a5`
Run ID: `volunteer-training-coordinator-with-anti-cheating-gradient-verification-ce097d80e3a5-20260613T064627675568+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e553faf733bb

## What looked useful

Gradient verification achieved mean cheating TPR 0.9143, honest false-positive rate 0.1153, safe assignment 0.3893, and unsafe cheater assignment 0.0685 over 64 seeds and 64,000 simulated volunteers. It improved TPR over static quiz by +0.8553 and reduced unsafe cheater assignment versus static quiz by -0.5461 absolute.

## Boundaries and scale limits

Synthetic-only evidence: no real volunteers, no live coordinator, no LLM or human text responses, no semantic grader, no adversarial adaptation after observing the verifier, and no field deployment. Results are bounded to the hand-coded response and cheating model.

## Claim scope

In a deterministic synthetic volunteer-training coordinator simulation, a three-step perturbed challenge ladder detects brittle canonical-answer cheating substantially better than no verification, a static quiz, or random spot checks, while modestly improving safe role assignment over no verification.

## Why it stopped

Synthetic/proxy-only mechanism evidence is not sufficient for a paper or deployment claim, even though it supports a bounded follow-up.

## Recommended next action

Stop this run as no-paper useful signal; next run should build a direct text-response benchmark with held-out perturbed volunteer scenarios and calibrated grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Text Benchmark for Volunteer Training Gradient Verification
- Success threshold: Gradient verification improves cheating TPR by >=0.25 over static quiz while keeping honest false-positive rate increase <=0.05 absolute and reducing unsafe cheater assignments by >=0.20 absolute.
- Stop condition: Stop as negative if gradient verification fails the TPR threshold or exceeds the FPR limit on held-out perturbed text responses.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-training-coordinator-with-anti-cheating-gradient-verification-ce097d80e3a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
