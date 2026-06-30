# SpecDec Tree Verification with No Draft VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `specdec-tree-verification-with-no-draft-vram-c02df782e8d4`
Run ID: `specdec-tree-verification-with-no-draft-vram-c02df782e8d4-20260610T160127936192+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1f41c074e5ce

## What looked useful

All four tested tree shapes passed packed-tree-vs-independent-path correctness checks in fp16. Target-only peak allocations ranged from 44.59 to 90.55 MiB; adding a simulated draft KV cache raised peak allocation by 2.62 to 10.19 MiB. This supports the mechanism but is not paper-ready.

## Boundaries and scale limits

No real draft model, real target model, tokenizer, acceptance loop, serving stack, or full profiler trace was tested. The draft-resident comparison is a simulated KV tensor, and throughput is synthetic target-verifier throughput rather than end-to-end speculative decoding speedup.

## Claim scope

Synthetic PyTorch target-verifier benchmark on NVIDIA GB10 shows packed speculative tree verification can run with draft proposals represented as CPU token IDs and parent indices, without allocating draft model parameters or draft KV cache on GPU in the target-only verification path.

## Why it stopped

Synthetic/proxy evidence supports the no-draft-VRAM verification mechanism, but this is not a full validation of real speculative decoding memory residency or speedup.

## Recommended next action

Run a bounded real-model integration using a small target model and CPU-side draft candidate generator, with profiler evidence that no draft parameters or draft KV remain resident on GPU and with accepted-token throughput measured.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model profiler test for no-draft-VRAM tree verification
- Success threshold: On a small real model, match autoregressive verification correctness, reduce peak GPU memory by at least the measured draft KV/parameter residency amount versus GPU-draft baseline, and lose no more than 20% accepted-token throughput on the tested prompt set.
- Stop condition: Stop if profiler traces show unavoidable draft KV or draft parameters on GPU during verification, or if CPU-to-GPU proposal transfer overhead causes more than 20% accepted-token throughput loss in the bounded test.

## Evidence references

- Artifact root: `<local-path>/projects/specdec-tree-verification-with-no-draft-vram-c02df782e8d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
