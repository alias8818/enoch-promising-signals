# SpecDec Tree Verification with KV-Collapse Bypass

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `specdec-tree-verification-with-kv-collapse-bypass-8ea2da31d7d4`
Run ID: `specdec-tree-verification-with-kv-collapse-bypass-8ea2da31d7d4-20260610T041911981344+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/89779ce81038

## What looked useful

The mechanism is worth a bounded end-to-end follow-up: duplicate verifier KV projection work grows with speculative tree depth/branching, and a cache layout that preserves accepted tree KV addresses can remove a small but consistent gather/copy cost. In this proxy, mean shared-tree speedup over path recomputation was 1.84x, mean bypass-over-collapse speedup was 1.064x, and mean bypass-over-baseline speedup was 1.94x.

## Boundaries and scale limits

Not an end-to-end language-model serving result. Uses synthetic embeddings/projections, deterministic accepted path, no real draft/target model agreement, no production cache manager, and no scheduler or batching effects.

## Claim scope

Synthetic GB10 GPU mechanism benchmark of speculative-decoding tree verification KV projection reuse and accepted-path KV-collapse bypass. Shared-prefix tree KV computation was faster than path recomputation in 4 of 5 benchmark cases, and bypassing accepted-path collapse was faster than explicit collapse in 5 of 5 cases.

## Why it stopped

Closed as no-paper useful signal: the result supports the mechanism in a synthetic proxy but does not directly validate full speculative decoding or production KV cache behavior.

## Recommended next action

Run a bounded end-to-end tiny-transformer speculative decoding implementation with real logits and KV cache layout ablations; stop short of paper claims until serving latency/tokens-per-second confirms the proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end tiny-transformer validation of tree KV-collapse bypass
- Success threshold: At least 1.15x end-to-end decode latency or tokens-per-second improvement over standard tree verification in two or more realistic acceptance regimes, with identical outputs and measured cache-copy reduction.
- Stop condition: Stop if end-to-end speedup is below 1.05x in all tested regimes or if cache-layout indirection overhead cancels the collapse-bypass benefit.

## Evidence references

- Artifact root: `<local-path>/projects/specdec-tree-verification-with-kv-collapse-bypass-8ea2da31d7d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
