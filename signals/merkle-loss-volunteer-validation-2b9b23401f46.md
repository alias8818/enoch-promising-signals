# Merkle-Loss Volunteer Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-loss-volunteer-validation-2b9b23401f46`
Run ID: `merkle-loss-volunteer-validation-2b9b23401f46-20260607T072808409334+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74310f1de90c

## What looked useful

A Merkle tree is useful as a commitment and lookup layer after a root is fixed, but inclusion-only volunteer checks pass even for a fully fabricated loss trace. Volunteer validation requires sampled recomputation from model state, data, batch metadata, and deterministic execution details; detection probability follows the sampled-leaf coverage curve.

## Boundaries and scale limits

512 synthetic steps, tiny MLP, single local GB10 GPU, in-memory model states, no real volunteer network, no LLM-scale training, no incentive/Sybil model, and no storage-efficient checkpoint protocol.

## Claim scope

Toy synthetic validation of Merkle commitments over per-step training losses for a tiny MLP trace: inclusion proofs are cheap and recomputation catches sampled fake losses, but Merkle loss roots alone do not validate truthfulness.

## Why it stopped

Early bounded falsification of standalone inclusion-only Merkle-loss validation; the positive mechanism requires recomputation evidence beyond a Merkle loss root.

## Recommended next action

Stop this run as a no-paper useful signal; deepen only with a real small language-model trace that includes checkpoint-stratified sampled recomputation and storage accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpoint-stratified Merkle-loss validation on a real small LM trace
- Success threshold: On at least a 10k-step small-LM trace, 64 sampled recomputations detect at least 95% of 5% random leaf tampering, honest recomputation has zero mismatches, and verifier cost plus checkpoint storage is explicitly reported.
- Stop condition: Stop if deterministic recomputation cannot be achieved from released checkpoints/batch metadata or if storage needed for sampled verification is too large to be practical for volunteer validators.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-loss-volunteer-validation-2b9b23401f46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
