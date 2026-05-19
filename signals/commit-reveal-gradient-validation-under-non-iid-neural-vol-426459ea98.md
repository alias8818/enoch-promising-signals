# Commit-Reveal Gradient Validation Under Non-IID Neural Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-validation-under-non-iid-neural-vol-426459ea98`
Run ID: `commit-reveal-gradient-validation-under-non-iid-neural-vol-426459ea98-20260518T124534322770+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bad98d7e7975

## What looked useful

Hash-based commit-reveal rejected all post-commit tampered reveals, but no validation-loss margin across lr 0.05, 0.1, 0.2, 0.4, and 0.8 accepted >=90% honest non-IID gradients while rejecting >=90% committed malicious gradients. Closest point was lr 0.05 margin 0.0 with 88.33% honest accept and 83.17% malicious reject.

## Boundaries and scale limits

Not foundation-model scale, not real volunteer networking, not exhaustive adaptive attacks, and not a proof against all validation designs. Direct only for the tested non-IID small neural setup and validation-loss gate.

## Claim scope

Small controlled CPU PyTorch test on scikit-learn digits with a one-hidden-layer MLP, 20 simulated non-IID volunteer clients, commit-reveal SHA-256 gradient hashes, and public validation-loss gating. Commit-reveal integrity was supported; the validation-loss gate failed the 90/90 honest-accept/malicious-reject threshold.

## Why it stopped

Tier 1 direct test falsified the explicit 90/90 validation threshold for this simple commit-reveal plus public validation-loss mechanism; this is not a full-scale impossibility result.

## Recommended next action

Run a bounded deepen test that augments validation-loss gating with norm clipping, cosine agreement to a public reference gradient, and repeated micro-batch validation challenges on the same 20-client non-IID benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust Commit-Reveal Gradient Validation With Public Reference Agreement
- Success threshold: At least one robust-gate setting achieves honest_accept_rate >= 0.90, committed_malicious_reject_rate >= 0.90, tamper_hash_reject_rate = 1.0, and aggregate validation loss improvement no worse than 25% below honest-only aggregate improvement.
- Stop condition: Stop if no robust-gate setting meets the 90/90 threshold after sweeping step sizes and margins comparable to this run, or if the robust gate meets classification rates but destroys aggregate learning progress.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-validation-under-non-iid-neural-vol-426459ea98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
