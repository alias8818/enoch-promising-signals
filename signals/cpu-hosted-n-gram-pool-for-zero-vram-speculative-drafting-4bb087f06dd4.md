# CPU-Hosted N-Gram Pool for Zero-VRAM Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-hosted-n-gram-pool-for-zero-vram-speculative-drafting-4bb087f06dd4`
Run ID: `cpu-hosted-n-gram-pool-for-zero-vram-speculative-drafting-4bb087f06dd4-20260525T184201572953+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f0343368d0fd

## What looked useful

CPU lookup is fast (<1 us p95 in Python), but the useful drafting signal collapses for token-like contexts: best word-level verifier-call reduction was 4.01% with a 1-word context, 1.88% with a 2-word context, 0.37% with a 3-word context, and effectively zero for 4-5 word contexts. Short character contexts showed larger proxy gains but are not representative of LLM token verification.

## Boundaries and scale limits

Tested one small public corpus, whitespace word tokens and character tokens, exact held-out replay oracle, no real target LLM, no BPE tokenizer, no GPU verifier, no batching or serving stack.

## Claim scope

On a local Tiny Shakespeare held-out replay proxy, a CPU-hosted exact-match n-gram continuation table has negligible lookup overhead and bounded memory, but token-like word-level continuation acceptance is too low to imply meaningful zero-VRAM speculative decoding speedup.

## Why it stopped

Proxy early falsification: the CPU table is feasible, but exact-match n-gram drafting did not produce enough token-like accepted draft tokens to justify a paper claim or larger serving validation from this run alone.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should be a model-in-the-loop BPE-token prompt-lookup variant only if the controller wants to deepen this exact mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Prompt-Local CPU N-Gram Drafting With Target-Model Verification
- Success threshold: At least 10% median end-to-end tokens/sec improvement over baseline on repetitive prompts, less than 5% regression on non-repetitive controls, and zero additional model VRAM for the drafter.
- Stop condition: Stop if BPE model-in-the-loop acceptance yields less than 5% verifier-call reduction or less than 5% end-to-end throughput improvement on the repetitive prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-hosted-n-gram-pool-for-zero-vram-speculative-drafting-4bb087f06dd4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
