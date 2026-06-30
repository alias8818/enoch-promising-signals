# 8-bit AdamW with sparse gradient accumulation for gb10 VRAM reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-with-sparse-gradient-accumulation-for-gb10-vram-reduction-feffb05d6947`
Run ID: `8-bit-adamw-with-sparse-gradient-accumulation-for-gb10-vram-reduction-feffb05d6947-20260609T175055289354+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2176f6fda42a

## What looked useful

8-bit AdamW is a practical GB10 memory reduction mechanism in this bounded test. Sparse accumulation is not paper-ready: 2% density reduced peak memory but hurt the loss proxy, while 10% density recovered the loss proxy but used more sparse-buffer memory than dense bf16 gradients and gave little extra peak-memory reduction beyond 8-bit AdamW.

## Boundaries and scale limits

Synthetic random-token data, 8 optimizer steps, about 69M parameters, Python/PyTorch top-k sparse accumulation with dense gradient rematerialization at optimizer step; not a real convergence run, not 7B+ scale, and not a fused production sparse-gradient kernel.

## Claim scope

On a GB10 CUDA transformer-shaped 69M-parameter proxy, bitsandbytes 8-bit AdamW reduced persistent optimizer-state bytes by 49.0% and CUDA max allocated by 16.2% versus dense AdamW with matching short-run loss; sparse top-k microbatch accumulation provided an additional peak reduction only at 2% density, where short-run loss worsened and throughput fell.

## Why it stopped

Bounded proxy evidence supports the 8-bit optimizer-state mechanism but leaves the combined sparse-accumulation claim mixed and not publication-grade.

## Recommended next action

Stop this run as no-paper useful signal; only revisit sparse accumulation with a fused implementation and real dataset convergence test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused sparse accumulation convergence test for 8-bit AdamW on GB10
- Success threshold: At least 15% lower CUDA max allocated than 8-bit AdamW alone, final validation loss within 1% of the 8-bit AdamW baseline over a bounded real-data run, and no more than 25% throughput loss.
- Stop condition: Stop if densities that preserve validation loss provide less than 10% extra peak-memory reduction versus 8-bit AdamW alone or if fused sparse accumulation remains more than 50% slower.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-sparse-gradient-accumulation-for-gb10-vram-reduction-feffb05d6947`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
