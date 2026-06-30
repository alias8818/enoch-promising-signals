# LLM-backed LangGraph doctrine memory under noisy verifier labels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `llm-backed-langgraph-doctrine-memory-under-noisy-verifier-52cbf9df84`
Run ID: `llm-backed-langgraph-doctrine-memory-under-noisy-verifier-52cbf9df84-20260630T123533389113+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Automatic Doctrine Memory in a Real Local Tool-Using Agent Harness: enoch://control-plane/projects/automatic-doctrine-memory-in-a-real-local-tool-using-agent-f8c81079a7/runs/automatic-doctrine-memory-in-a-real-local-tool-using-agent-f8c81079a7-20260630T115803663179+0000
- Parent run decision: Doctrine memory in a real LangGraph tool-agent with noisy verifier feedback: enoch://control-plane/projects/doctrine-memory-in-a-real-langgraph-tool-agent-with-noisy-9aad556b20/runs/doctrine-memory-in-a-real-langgraph-tool-agent-with-noisy-9aad556b20-20260630T121903411539+0000

## What looked useful

Persistent doctrine memory beat a stateless baseline when noisy verifier labels were better than chance, with mean naive-counter accuracy 0.940 at 30% noise and 0.765 at 40% noise versus 0.506 stateless. At 49% noise, the memory advantage shrank to 0.552 versus 0.506. The gated beta updater did not outperform the naive counter at any tested noise rate.

## Boundaries and scale limits

No real LLM, no natural-language verifier rationales, no multi-step agent traces, no long-term semantic memory store, and no production verifier. Results only support this small binary-rule proxy.

## Claim scope

Synthetic LangGraph proxy with 12 binary doctrines, 144 training episodes per run, 40 paired seeds, and Bernoulli verifier-label flip rates from 0.00 to 0.49. LangGraph MemorySaver checkpointed state was directly exercised; real LLM doctrine editing was proxied by a deterministic doctrine-revision node.

## Why it stopped

Proxy evidence is mixed: LangGraph checkpointed memory is useful under moderate label noise, but the proposed confidence-gated doctrine memory did not beat a simple counter and the LLM-backed portion was not directly tested.

## Recommended next action

Stop this run as no-paper useful-signal evidence; run one bounded deepen follow-up with a real small LLM doctrine summarizer and realistic verifier rationales before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM doctrine summaries under noisy verifier rationales
- Success threshold: At least +5 percentage points final doctrine accuracy over the simple structured-memory counter at 30-45% verifier noise, with no higher corruption rate and all checkpoint persistence checks passing.
- Stop condition: Stop if the LLM-backed updater is within +/-2 percentage points of the counter across 30-45% noise or has a higher corruption rate in paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/llm-backed-langgraph-doctrine-memory-under-noisy-verifier-52cbf9df84`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
