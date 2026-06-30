# VerifiableForwardPassPuzzles

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiableforwardpasspuzzles-10e1a141b3ff`
Run ID: `verifiableforwardpasspuzzles-10e1a141b3ff-20260619T153252067367+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/8a8b14f4b5cd

## What looked useful

Exact recomputation detected all tampering but had median verification/solve ratio 0.9838405146. Trusted digest checking had median cost ratio 0.0040317406 but detected only output-affecting tampering in this setup. Sampled row audits used 0.9375% to 30% of full multiply-adds and detected 52.5% to 98.75% of random tamper trials, with misses recorded in results/failure_cases.json.

## Boundaries and scale limits

Tested 80 synthetic puzzles at dimensions 128,128,128,64 on a single CPU process, with random rather than adversarially optimized tampering. Did not test real model inference, GPUs, cryptographic proof systems, or economic proof-of-work security.

## Claim scope

For small deterministic integer MLP forward-pass puzzles with public weights, inputs, claimed activation transcripts, and output hashes, exact public verification costs essentially the same as solving; sampled transcript auditing is faster but probabilistic and can miss tampering.

## Why it stopped

Bounded synthetic evidence is an early falsification of cheap exact public verification for the tested construction, not a full validation of all forward-pass puzzle designs.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run one bounded deepen test with Merkle-committed activation transcripts and adversarially selected corruptions against the sampled row-audit baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkle-committed activation transcript audits for forward-pass puzzles
- Success threshold: At least 99% detection of adversarial single-layer tampering with verification cost below 20% of full forward-pass multiply-adds and reproducible proof-size metrics.
- Stop condition: Stop if adversarial tampering detection stays below 95% at 20% verification cost or if proof material makes verification plus transmission more expensive than exact recomputation.

## Evidence references

- Artifact root: `<local-path>/projects/verifiableforwardpasspuzzles-10e1a141b3ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
