# ChunkLion: chunk-wise variance-corrected Lion for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `chunklion-chunk-wise-variance-corrected-lion-for-tiny-vram-training-7a8d6b9f6253`
Run ID: `chunklion-chunk-wise-variance-corrected-lion-for-tiny-vram-training-7a8d6b9f6253-20260612T022800079410+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b166d9d7a0eb

## What looked useful

Chunk-wise variance state can be stored with only about 0.05% extra optimizer-state bytes over Lion and about half AdamW state, but the tested correction did not beat Lion on validation loss or stability and reduced throughput by roughly 20-27% in the prototype.

## Boundaries and scale limits

Synthetic data, small model, short 250-step runs, no real corpus, no GPT-2-small-class baseline, no explicit tiny-VRAM cap, no activation-checkpointing/offload scenario, and no large learning-rate or hyperparameter sweep beyond a small Lion-vs-ChunkLion stress probe.

## Claim scope

On a local small GPT-style causal LM trained on deterministic synthetic Markov-token data for 250 steps across three seeds, ChunkLion achieved the intended near-Lion optimizer-state memory but did not improve validation loss or high-learning-rate stability versus plain Lion and was slower in this prototype.

## Why it stopped

Early proxy falsification: the directly tested small-GPU causal-LM runs support the state-memory saving but do not support the added chunk-wise variance correction as better than plain Lion; full-scale evidence would be required to overturn this proxy result.

## Recommended next action

Stop this idea as a no-paper local result unless a future project changes the mechanism or tests a different memory-saving optimizer family against Lion, Adafactor, 8-bit optimizers, and AdamW on a real corpus.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/chunklion-chunk-wise-variance-corrected-lion-for-tiny-vram-training-7a8d6b9f6253`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
